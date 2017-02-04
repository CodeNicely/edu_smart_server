from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.models import students_data
from teachers.models import teachers_data
from general.models import KEYS
import jwt
from django.http import JsonResponse
@csrf_exempt
def login(request):
	response={}
	if(request.method=='POST'):
		try:
			user_type=int(request.POST.get("user_type"))
			print "user_type",user_type
			#user_type 0 teacher
			#user_type 1 student
			if(user_type==0):
				roll_no_get=request.POST.get("roll_no")
				print roll_no_get
				teacher=teachers_data.objects.get(roll_no=roll_no_get)
				if(teacher!=None):
					password=hashlib.sha512(request.POST.get("password")).hexdigest().lower()
					if(teacher.password==password):
						response['success']=True
						response['message']="Permission Granted"
						response['access_token']=jwt.encode({'roll_no':roll_no_get,"user_type":user_type}, str(KEYS.objects.get(key='jwt').value), algorithm='HS256')
					else:
						response['success']=False
						response['message']="Permission Denied"
				else:
					response['success']=False
					response['message']="No such entry found"

			if(user_type==1):
				roll_no_get=request.POST.get("roll_no")
				print roll_no_get
				student=students_data.objects.get(roll_no=roll_no_get)
				if(student!=None):
					password=hashlib.sha512(request.POST.get("password")).hexdigest().lower()
					if(student.password==password):
						response['success']=True
						response['message']="Permission Granted"
						response['access_token']=jwt.encode({'roll_no':roll_no_get,"user_type":user_type}, str(KEYS.objects.get(key='jwt').value), algorithm='HS256')
					else:
						response['success']=False
						response['message']="Permission Denied"
				else:
					response['success']=False
					response['message']="No such entry found"
			else:
				response['success']=False
				response['message']="wrong user type"
		except Exception,e:
			response['success']=False
			response['message']=str(e)

	if(request.method=='GET'):
		response['success']=False
		response['messgae']="Not POST method"
		
	print response
	return JsonResponse(response)