from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from general.models import KEYS_internal
from .models import *
def splash_screen(request):
	response_json={}
	if request.method=='GET':
		try:
			version=int(KEYS_internal.objects.get(key='version').value)
			compulsory_update=KEYS_internal.objects.get(key='compulsory_update').value
			response_json['version']=version
			if int(compulsory_update)==1:
				response_json['compulsory_update']=True
			if int(compulsory_update)==0:
				response_json['compulsory_update']=False
			response['success']=True
			response['message']="Successful"
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	else:
		response_json['success']=False
		response_json['message']="not get method"
	print response_json
	return JsonResponse(response_json)