from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import *
from classes.models import *
from subjects.models import *
def file(name):
	img_ext=['JPEG|JFIF|EXIF|TIFF|GIF|BMP|PNG|PPM|PGM|PBM|PNM'].split('|')
	video_ext=['WEBM|MKV|FLV|VOB|GIF|GIFV|AVI|WMV'].split('|')
	pdf_ext=['PDF']

	if(name in img_ext):
		return 0
	if(name in video_ext):
		return 1
	if(name in pdf_ext):
		return 2
	return 3

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
				file_name+=file
				fout = open(file_name,'w')
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
				class_assignments.objects.create(title=title,description=description,file=file_name,subject=subjects_data.objects.get(id=subject_id))
			elif (file_upload_type==2):
				class_announcements.objects.create(title=title,description=description,file=file_name,subject=subjects_data.objects.get(id=subject_id))
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


#type=0 for heading
#type=1 for subject
#type=2 for assignments
#type=3 for announcements
#type=4 for notice
#type=5 for resources
#type=6 for syllabus
def data(request):
	response={}
	if(request.method=="GET"):
		try:
			subject_id=int(request.GET.get('subject_id'))
			data_type=int(request.GET.get('data_type'))
			data_list=[]
#			if(data_type==0):
#			if(data_type==1):
			if(data_type==2):
				for o in class_assignments.objects.all():
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['description']=o.description
					tmp_json['author']=o.author
					tmp_json['deadline']=o.deadline
					tmp_json['created']=str(o.created)[:18]
					data_list.append(tmp_json)
			if(data_type==3):
				for o in class_announcements.objects.all():
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['description']=o.description
					tmp_json['author']=o.author
					tmp_json['created']=str(o.created)[:18]
					data_list.append(tmp_json)
			if(data_type==6):
				for o in subjects_syllabus.objects.all():
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['description']=o.description
					data_list.append(tmp_json)
			if(data_type==5):
				for o in subjects_resources.objects.all():
					tmp_json={}
					tmp_json['title']=o.title
					tmp_json['file']=request.scheme+'://'+request.get_host()+'/'+str(o.file)
					tmp_json['created']=str(o.created)[:18]
					data_list.append(tmp_json)

			response['success']=True
			response['message']="Sucessfull"
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	else:
		response['success']=False
		response['message']="not get method"