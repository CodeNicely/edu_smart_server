from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.models import students_data
from teachers.models import teachers_data
from general.models import KEYS_internal
import jwt
from django.http import JsonResponse
from classes.models import class_data
from teachers.models import teachers_data
from students.models import students_data,students_in_class_data
from subjects.models import subjects_data
from general.models import notice_data
from classes.models import class_announcements,class_assignements
@csrf_exempt
def login(request):
	response={}
	if(request.method=='GET'):
		try:
			access_token=request.POST.get('access_token')
			print "access_token",access_token
			#user_type 0 teacher
			#user_type 1 student
			json_decoded=jwt.decode(str(access_token),str(KEYS_internal.objects.get(key='jwt').value), algorithms=['HS256'])
			roll_no=json_decoded['roll_no']
			user_type=json_decoded['user_type']
			if(user_type==0 or user_type==1):
				response['success']=True
				subjects_all=subjects_class_teacher_data.objects.all()
				
				class_all=class_data.objects.all()
				
				students_all=students_in_class_data.objects.all()
				
				notice_list=notice_data.objects.all()
				assignments_all=class_assignements.objects.all()
				announcements_all=class_announcements.objects.all()
				data_list=[]
				if(user_type==0):
					teacher=teachers_data.objects.get(roll_no=roll_no)
					subject_list=subjects_all.filter(teacher=teacher.id)

					#type=0 for heading
					#type=1 for subject
					#type=2 for assignments
					#type=3 for announcements
					#type=4 for notice

					###############################################################################################
					count=notice_list.count()
					if(count>4):
						count=4
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Notice"
					data_list.append(tmp_json)
					for o in notice_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['author']=o.author
						tmp_json['created']=str(o.created)[:18]
						tmp_json['type']=4
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					count=subject_list.count()
					if(count>4):
						count=4
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Subjects"
					data_list.append(tmp_json)
					for o in subject_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						class_object=class_all.get(id=o.class_id)
						tmp_json['department']=class_object.department
						tmp_json['name']=class_object.name
						tmp_json['type']=1
						tmp_json['student_count']=students_all.filter(class_name=class_object.id).count()
						data_list.append(tmp_json)
					###################################################################################################
					##################################################################################################3
					#################################################################################################
					###################################################################################################
					##################################################################################################3
					###################################################################################################
					##################################################################################################3

				if(user_type==1):
					student=students_data.objects.get(roll_no=roll_no)

					#type=0 for heading
					#type=1 for subject
					#type=2 for assignments
					#type=3 for announcements
					#type=4 for notice

					###############################################################################################
					count=notice_list.count()
					if(count>4):
						count=4
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Notice"
					data_list.append(tmp_json)
					for o in notice_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['author']=o.author
						tmp_json['created']=str(o.created)[:18]
						tmp_json['type']=4
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Subjects"
					data_list.append(tmp_json)
					subject_list=subjects_all.filter(class_id=students_all.get(student=student.id).class_name)
					count=subject_list.count()
					if(count>4):
						count=4
					for o in subject_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						subject=subjects_data.objects.get(id=o.subject)
						tmp_json['name']=subject.name
						tmp_json['type']=1
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Announcements"
					data_list.append(tmp_json)
					announcements_list=announcements_all.filter(class_id=students_all.get(student=student.id).class_name)
					count= announcements_list.count()
					if(count>4):
						count=4
					for o in announcements_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						#subject=subjects_data.objects.get(id=o.subject)
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['type']=3
						data_list.append(tmp_json)
					###################################################################################################

					################################################################################################
					tmp_json={}
					tmp_json['type']=0
					tmp_json['title']="Assignements"
					data_list.append(tmp_json)
					assignements_list=assignements_all.filter(class_id=students_all.get(student=student.id).class_name)
					count= announcements_list.count()
					if(count>4):
						count=4
					for o in assignements_list.order_by("created").reverse()[0:count]:
						tmp_json={}
						#subject=subjects_data.objects.get(id=o.subject)
						tmp_json['title']=o.title
						tmp_json['description']=o.description
						tmp_json['type']=2
						data_list.append(tmp_json)
					###################################################################################################


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