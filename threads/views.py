from django.shortcuts import render
from notification import send_notification
from .models import *
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import multiprocessing as mp
import jwt
from general.models import KEYS
from classes.models import class_data
from teachers.models import teachers_data
from students.models import students_data,students_in_class_data
from subjects.models import subjects_data,subjects_class_teacher_data
from general.models import notice_data
from classes.models import class_announcements,class_assignments

@csrf_exempt
def messaging(request):
	response={}
	if(request.method=='GET'):
		message_list=[]

		access_token=request.GET.get('access_token')
		print "access_token",access_token
		#user_type 0 teacher
		#user_type 1 student

		json_decoded=jwt.decode(str(access_token),str(KEYS.objects.get(key='jwt').value), algorithms=['HS256'])
		id=json_decoded['id']
		user_type=json_decoded['user_type']
		
		last_message_id=int(request.GET.get('last_message_id'))
		thread_id=int(request.GET.get('thread_id'))
		for o in message_data.objects.filter(thread_id=thread_id):
			if(o.id>last_message_id):
				tmp_response={}
				if(o.author_id==id):
					tmp_response['owner']=True
				else:
					tmp_response['owner']=False
				tmp_response['body']=o.message
				tmp_response['author_name']=o.author_name
				tmp_response['message_id']=o.id
				tmp_response['created']=str(o.created)[:18]
				message_list.append(tmp_response)
		
		response['success']=True
		response['message_list']=message_list

	if(request.method=='POST'):
		try:
			try:
				message_type=int(request.POST.get('message_type'))
			except:
				message_type=0
			access_token=request.POST.get('access_token')
			print "access_token",access_token
			#user_type 0 teacher
			#user_type 1 student

			json_decoded=jwt.decode(str(access_token),str(KEYS.objects.get(key='jwt').value), algorithms=['HS256'])
			id=json_decoded['id']
			print"id",id
			user_type=json_decoded['user_type']

			body=request.POST.get('message')
			print"body",body
			thread_id=int(request.POST.get('thread_id'))
			
			try:
				thread=thread_data.objects.get(id=thread_id)
				fcm_list=[]
				if(thread.access_level==0):
					for o in students_data.objects.all():
						fcm_list.append(o.fcm)
					for o in teachers_data.objects.all():
						fcm_list.append(o.fcm)
				if(thread.access_level==1):
					if(user_type==0):
						department=teachers_data.objects.get(id=id).department
						for o in students_data.objects.filter(department=department):
							fcm_list.append(o.fcm)
						for o in teachers_data.objects.filter(department=department):
							fcm_list.append(o.fcm)

					if(user_type==1):
						department=students_data.objects.get(id=id).department
						for o in students_data.objects.filter(department=department):
							fcm_list.append(o.fcm)
						for o in teachers_data.objects.filter(department=department):
							fcm_list.append(o.fcm)

				if(thread.access_level==2):
					if(user_type==1):
						class_name=class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name)
						for o in students_in_class_data.objects.filter(class_name=class_name).student:
							fcm_list.append(o.fcm)
						for o in subjects_class_teacher_data.objects.filter(class_id=class_name).teacher:
							fcm_list.append(o.fcm)

				print "80"
				try:
					teacher=teachers_data.objects.get(id=id)
					author=teacher.name
				except:
					pass
				try:
					student=students_data.objects.get(id=id)
					author=student.name
				except:
					pass
				message_data.objects.create(thread_id=thread,author_id=id,author_name=author,message=body)
				print "82"
				response['success']=True
				response['message']='message sent'

				#fcm_list=(o.fcm for o in user_list)
				fcm_safe=list(set(fcm_list))
				for o in fcm_safe:
					print "Sending fcm",o
					send_notification(o,1,"New Message")
				print "91"
			except Exception,e:
				print e
				response['success']=True
				response['message']='Some Error '+str(e)

			# divide_notification(1,['cZOs5H9v1xo:APA91bEYrrLLWvlpl5q-kg9rbd4s_B0NYJU3d3R-InyMrEw0TZcNGeI1AQt6AIffb6Jf0gqj1kuEUopwpJMu6X_AiFUcKjFHLCDcETO71cGgcq-UL-1fwBMI8ebGdNubrHW28l1p6BzH','dcmC6deDQHY:APA91bHSI28SSbpJEyLLq_BoSGkejIhApqLdHXzA0AzR3REmVCFZmI5jeiukOzqXlq1tRSMf_VOAnpC36mitM5o05wxQk1Zjcoo5xiNU0zssGvRpp5hpBCWtLRkFwacQrPKLLC0BlnV9',],"new  message")
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	print response
	return JsonResponse(response)
@csrf_exempt
def threading(request):
	response={}
	if(request.method=='GET'):
		try:
			access_token=request.GET.get('access_token')
			access_level=request.GET.get('access_level')
			json_decoded=jwt.decode(str(access_token),str(KEYS.objects.get(key='jwt').value), algorithms=['HS256'])
			id=json_decoded['id']
			user_type=json_decoded['user_type']
			print"109"
			data_array=[]
			for o in thread_data.objects.all():

				flag=0
				if(o.access_level==0):
					flag=1
				if(o.access_level==1):
					if(user_type==0):
						if(o.department==teachers_data.objects.get(id=id).department):
							flag=1
					if(user_type==1):
						if(o.department==class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name).department):
							flag=1
				if(o.access_level==2):
					if(user_type==0):
						class_id_array=[]
						for x in subjects_class_teacher_data.objects.filter(teacher=id):
							class_id_array.append(x.class_id)
						if(o.class_id in class_id_array):
							flag=1
					if(user_type==1):
						if(o.class_id==class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name)):
							flag=1
				print"168"
				if(flag==1):
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['thread_id']=o.id
					tmp_json['access_level']=o.access_level
					tmp_json['author']=o.author
					tmp_json['created']=str(o.created)[:18]
					tmp_json['description']=o.description
					data_array.append(tmp_json)
			print "178"
			response['data_list']=data_array
			response['success']=True
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	if(request.method=='POST'):
		try:
			access_token=request.POST.get('access_token')
			print 'access_token',access_token
			access_level=int(request.POST.get('access_level'))
			print 'access_level',access_level
			title=request.POST.get('title')
			print 'title',title
			description=request.POST.get('description')
			print 'description',description
			json_decoded=jwt.decode(str(access_token),str(KEYS.objects.get(key='jwt').value), algorithms=['HS256'])
			print"153"
			id=json_decoded['id']
			user_type=json_decoded['user_type']
			print user_type
			#access_level=request.POST.get['access_level']
			print"157"
			try:
				teacher=teachers_data.objects.get(id=id)
				author=teacher.name
			except:
				pass
			try:
				student=students_data.objects.get(id=id)
				author=student.name
			except:
				pass

			# class_id=students_in_class_data.objects.get(student=id).class_name
			# print "class_id",class_id
			# class_inst=class_data.objects.get(id=class_id.id)
			# print "class_int",class_inst
			# dept_ins=department_data.objects.get(id=class_inst.id)
			# print "dept_ins",dept_ins
			if(access_level==0):
				thread_data.objects.create(title=title,access_level=access_level,description=description,author=author)
			if(access_level==1):
				if(user_type==0):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=teacher.department,author=author)
				if(user_type==1):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=dept_ins)
			if(access_level==2):
				if(user_type==0):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=teacher.department,author=author)
				if(user_type==1):
					thread_data.objects.create(title=title,access_level=1,description=description,author=author,class_id=class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name).department)
			response['success']=True
			response['message']="Thread Created"		
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	print response
	return JsonResponse(response)