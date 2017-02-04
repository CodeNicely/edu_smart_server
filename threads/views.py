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

		for o in message_data.objects.all():
			if(o.id>last_message_id):
				tmp_response={}
				if(o.author_id==id):
					tmp_response['owner']=True
				else:
					tmp_response['owner']=False
				tmp_response['body']=o.author_name
				tmp_response['message_id']=o.id
				tmp_response['created']=str(o.created)[:18]
				message_list.append(tmp_response)
		
		response['success']=True
		response['message_list']=message_list

	if(request.method=='POST'):
		try:
			message_type=int(request.POST.get('message_type'))
			user_id=request.POST.get('access_token')
			body=request.POST.get('message')
			
			try:
				if message_type==1:
					image=request.FILES.get('image_name').name
					folder = 'media/'
					os.mkdir(os.path.join(folder))
					fout = open(folder+image,'w')
					file_content = request.FILES.get('image').read()
					#for chunk in file_content.chunks():
					fout.write(file_content)
					fout.close()
					image_location=folder+image
					message_data.objects.create(user_id=user_id,message="Image Message",type=1,image_url=image_location)
				else:
					message_data.objects.create(user_id=user_id,message=body)
				response['success']=True
				response['message']='message sent'
				user_list=user_data.objects.all()
				fcm_list=(o.fcm for o in user_list)
				fcm_safe=list(set(fcm_list))
				for o in fcm_safe:
					print "Sending fcm"
					send_notification(o,1,"New Message")
				print "59"
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
						for x in subjects_class_teacher_data.objects.filter(taecher=id):
							class_id_array.append(x.class_id)
						if(o.class_id in class_id_array):
							flag=1
					if(user_type==1):
						if(o.class_id==class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name)):
							flag=1
				if(flag==1):
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['thread_id']=o.id
					tmp_json['author']=o.author
					tmp_json['created']=str(o.created)[:18]
					tmp_json['description']=o.description
					data_array.append(tmp_json)
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

			if(access_level==0):
				thread_data.objects.create(title=title,access_level=access_level,description=description,author=author)
			if(access_level==1):
				if(user_type==0):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=teacher.department,author=author)
				if(user_type==1):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name).department,author=author)
			if(access_level==2):
				if(user_type==0):
					thread_data.objects.create(title=title,access_level=access_level,description=description,department=teacher.department,author=author)
				if(user_type==1):
					thread_data.objects.create(title=title,access_level=1,description=description,author=author,department=class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name).department)
			response['success']=True
			response['message']="Thread Created"		
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	print response
	return JsonResponse(response)