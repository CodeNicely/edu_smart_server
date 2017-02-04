from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *
def welcome(request):
	response_json={}
	if request.method=='GET':
		for x,y in request.GET.items():
			print "key,value ",x,":",y
		slider_list=[]
		for o in welcome_data.objects.all():
			welcome_details={}
			welcome_details['welcome_id']=str(o.id);
			welcome_details['image']=request.scheme+'://'+request.get_host()+'/media/'+str(o.image);
			welcome_details['quote']=str(o.quote);
			
			slider_list.append(welcome_details)
		response_json['success'] = True
		response_json['message'] = 'Successful'
		response_json['slider_list']=slider_list
	else:
		response_json['success']=False
		response_json['message']="not get method"
	print response_json
	return JsonResponse(response_json)
