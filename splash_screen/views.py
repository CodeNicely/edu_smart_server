from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from general.models import KEYS
from .models import *
def splash(request):
	response={}
	if request.method=='GET':
		try:
			version=int(KEYS.objects.get(key='version').value)
			compulsory_update=KEYS.objects.get(key='compulsory_update').value
			response['version']=version
			if int(compulsory_update)==1:
				response['compulsory_update']=True
			if int(compulsory_update)==0:
				response['compulsory_update']=False
			response['success']=True
			response['message']="Successful"
		except Exception,e:
			response['success']=False
			response['message']=str(e)
	else:
		response['success']=False
		response['message']="not get method"
	print response
	return JsonResponse(response)