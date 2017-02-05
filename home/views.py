from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.models import students_data
from teachers.models import teachers_data
from general.models import KEYS
import jwt
from django.http import JsonResponse
from classes.models import class_data
from teachers.models import teachers_data
from students.models import students_data,students_in_class_data
from subjects.models import subjects_data,subjects_class_teacher_data
from general.models import notice_data
from classes.models import class_announcements,class_assignments

#type=0 for heading
#type=1 for subject
#type=2 for assignments
#type=3 for announcements
#type=4 for notice
#type=5 for resources
#type=6 syllabus
@csrf_exempt
def home(request):
	response={}
	if(request.method=='GET'):
		try:
			access_token=request.GET.get('access_token')
			fcm=request.GET.get('fcm')
			print "access_token",access_token
			#user_type 0 teacher
			#user_type 1 student
			print"37"
			json_decoded=jwt.decode(str(access_token),str(KEYS.objects.get(key='jwt').value), algorithms=['HS256'])
			id=json_decoded['id']
			user_type=json_decoded['user_type']
			if(user_type==0 or user_type==1):
				response['success']=True
				notice_list=notice_data.objects.all()
				data_list=[]
				print"37"
				if(user_type==0):
					teacher=teachers_data.objects.get(id=id)
					teacher.fcm=fcm
					teacher.save()
					count=notice_list.count()
					if(count>4):
						count=4
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Notice"
					data_list.append(tmp_json)
					for o in notice_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['author']=o.author
						tmp_json['created']=str(o.created)[:18]
						tmp_json['card_type']=4
						data_list.append(tmp_json)
					print "53"
					###################################################################################################

					################################################################################################
					
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Subjects"
					data_list.append(tmp_json)
					subject_list=subjects_class_teacher_data.objects.filter(teacher=teachers_data.objects.get(id=id))
					count=subject_list.count()
					# if(count>4):
					# 	count=4
					for o in subject_list.all():
						tmp_json={}
						# class_object=class_all.get(id=)
						tmp_json['department']=o.subject.department.name
						tmp_json['title']=o.subject.name
						tmp_json['card_type']=1
						tmp_json['id']=o.subject.id
						#tmp_json['count']=students_in_class_data.objects.filter(class_name=o.class_id).count()
						data_list.append(tmp_json)
					###################################################################################################
					print"75"
					response['home_data_list']=data_list
					response['success']=True
				elif user_type==1 :
					student=students_data.objects.get(id=id)
					student.fcm=fcm
					student.save()
					print "89"
					#student=students_data.objects.get(id=id)
					count=notice_list.count()
					if(count>4):
						count=4
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Notice"
					data_list.append(tmp_json)
					for o in notice_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['author']=o.author
						tmp_json['created']=str(o.created)[:18]
						tmp_json['card_type']=4
						data_list.append(tmp_json)
					###################################################################################################
					print"107"
					class_id=students_in_class_data.objects.get(student=student.id).class_name
					print"109"
					################################################################################################
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Subjects"
					data_list.append(tmp_json)
					subject_list=subjects_class_teacher_data.objects.filter(class_id=class_id)
					count=subject_list.count()
					for o in subject_list[0:count]:
						tmp_json={}
						#subject=subjects_data.objects.get(id=o.subject)
						tmp_json['title']=o.subject.name
						tmp_json['id']=o.subject.id
						tmp_json['card_type']=1
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Announcements"
					data_list.append(tmp_json)
					announcements_list=class_announcements.objects.filter(class_id=class_id)
					count= announcements_list.count()
					if(count>4):
						count=4
					for o in announcements_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						#subject=subjects_data.objects.get(id=o.subject)
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['card_type']=3
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					tmp_json={}
					tmp_json['card_type']=0
					tmp_json['title']="Assignements"
					data_list.append(tmp_json)
					assignements_list=class_assignments.objects.filter(class_id=class_id)
					count= assignements_list.count()
					if(count>4):
						count=4
					for o in assignements_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						#subject=subjects_data.objects.get(id=o.subject)
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['card_type']=2
						data_list.append(tmp_json)
					###################################################################################################
					response['home_data_list']=data_list
					response['success']=True
				else:
					response['success']=False
					response['message']="user not found"
			else:
				response['success']=False
				response['message']="invalid user type"
		except Exception,e:
			response['success']=False
			response['message']=str(e)

	if(request.method=='POST'):
		response['success']=False
		response['message']="Not get method"
	print response
	return JsonResponse(response)