from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.models import students_data
from teachers.models import teachers_data
from general.models import KEYS_internal
import jwt
from django.http import JsonResponse
from teachers.models import teachers_data
from students.models import students_data
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
			if(user_type==0):
				teacher=teachers_data.objects.get(roll_no=roll_no)
				if(student!=None):
					pass
			elif(user_type==1):
				student=students_data.objects.get(roll_no=roll_no)
				if(student!=None):
					pass
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