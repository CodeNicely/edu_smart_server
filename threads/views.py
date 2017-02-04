from django.shortcuts import render
from notification import send_notification
from .models import *
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import multiprocessing as mp

@csrf_exempt
def messaging(request):
	response={}
	if(request.method=='GET'):
		message_list=[]
		user_id=request.GET.get('access_token')
		
		try:
			last_message_id=request.GET.get('last_message_id')
		except Exception,e:
			last_message_id=-9999
			print "Last message id not found",str(e)

		fcm=request.GET.get('fcm')
		user_details=user_data.objects.get_or_create(user_id=user_id,fcm=fcm)

		print fcm
		message_list1=message_data.objects.all()
		print str(message_list1)
		if last_message_id==-9999:
			for o in message_data.objects.all()[30:]:
				tmp_response={}
				if(o.user_id==user_id):
					tmp_response['owner']=True
				else:
					tmp_response['owner']=False
				tmp_response['body']=o.message
				tmp_response['user_id']=o.user_id
				tmp_response['message_id']=o.id
				tmp_response['created']=str(o.created)[:18]
				message_list.append(tmp_response)

		else:
			for o in message_data.objects.all().filter(id__gt=last_message_id):
				tmp_response={}
				if(o.user_id==user_id):
					tmp_response['owner']=True
				else:
					tmp_response['owner']=False
				tmp_response['user_id']=o.user_id
				tmp_response['body']=o.message
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

def threading(request):
	response={}
	if(request.method=='GET'):
		try:
			access_token=request.GET.get('access_token')
			access_level=request.GET.get('access_level')
			json_decoded=jwt.decode(str(access_token),str(KEYS_internal.objects.get(key='jwt').value), algorithms=['HS256'])
			id=json_decoded['id']
			user_type=json_decoded['user_type']
			for o in thread_data.objects.all():
				data_array=[]
				flag=0
				if(o.access_level==0):
					flag=1
				if(o.access_level==1):
					if(user_type==0):
						if(o.department==teacher_data.objects.get(id=id).department):
							flag=1
					if(user_type==1):
						if(o.department==class_data.objects.get(id=students_in_class_data.objects.get(teacher=id).class_name).department)
						flag=1
				if(o.access_level==2):
					if(user_type==0):
						class_id_array=[]
						for x in subjects_class_teacher_data.objects.filter(taecher=id):
							class_id_array.append(x.class_id)
						if(o.class_id in class_id_array):
							flag=1
					if(user_type==1):
						if(o.class_id==class_data.objects.get(id=students_in_class_data.objects.get(student=id).class_name))
						flag=1
				if(flag==1):
					tmp_json={}
					tmp_json['title']=o.title
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
			access_level=request.POST.get('access_level')
			title=request.POST.get('title')
			description=request.POST.get('description')
			json_decoded=jwt.decode(str(access_token),str(KEYS_internal.objects.get(key='jwt').value), algorithms=['HS256'])
			id=json_decoded['id']
			user_type=json_decoded['user_type']
			access_level=request.POST.get['access_level']
			if(access_level==0):
				thread_data
			if(user_type==0):
			if(user_type==1):

		except Exception,e:
			response['success']=False
			response['message']=str(e)

	return JsonResponse(response)