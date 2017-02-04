from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import *
@csrf_exempt
def file_upload(request):
	response={}
	if(request.method=='POST'):
		try:
			file_upload_type=int(request.POST.get('type'))
			#type=0 resource
			#type=1 assignment
			#type=2 announcement
			file=request.FILES.get('file').name
			print file
			if(str(file)!="None"):
				print "line 19"
				file_name='media/resources/'+str(timezone.now())[:18].replace(" ", "")
				fout = open(file_name+file,'w')
				print "line 21"
				file_content = request.FILES.get('file').read()
				fout.write(file_content)
				fout.close()
				print"file created"
			subject_id=int(request.POST.get('subject_id'))
			title=request.POST.get('title')
			description=request.POST.get('description')
			response['success']=True
			response['message']="file uploaded"
			if(file_upload_type==0):
				subjects_resources.objects.create(title=title,description=description,file=file_name,subject=subjects_data.objects.get(id=subject_id))
			elif (file_upload_type==1):
				subjects_assignments.objects.create(title=title,description=description,file=file_name,subject=subjects_data.objects.get(id=subject_id))
			elif (file_upload_type==2):
				subjects_announcements.objects.create(title=title,description=description,file=file_name,subject=subjects_data.objects.get(id=subject_id))
			else:
				response['success']=False
				response['message']="problem in type"
			
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	else:
		response['success']=False
		response['message']="Not get method"
	print response
	return JsonResponse(response)

