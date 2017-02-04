from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.models import students_data
from teachers.models import teachers_data
from general.models import KEYS
import jwt
from django.http import JsonResponse
from sms import send_sms

def hide(word):
	word_array=word.split('@')
	result = ""
	result=word_array[0][:3]
	for letter in word_array[0][3:]:
		result += "*"
	try:
		tmp=word_array[1]
		result+='@'
		result+=word_array[1]
	except:
		pass
	return result
import random
@csrf_exempt
def login(request):
	response={}
	if(request.method=='POST'):
		try:
			user_type=int(request.POST.get("login_type"))
			print "user_type",user_type
			#user_type 0 teacher
			#user_type 1 student
			if(user_type==0):
				id_get=request.POST.get("roll_no")
				print id_get
				teacher=teachers_data.objects.get(id=id_get)
				if(teacher!=None):
					otp=str(random.randint(999,9999))
					send_sms(teacher.mobile,"Otp for the app is "+otp)
					teacher.otp=otp
					teacher.save()
					response['success']=True
					response['message']="An otp has been sent to your email:"+hide(teacher.email)+" and to mobile:"+hide(teacher.mobile)

				else:
					response['success']=False
					response['message']="No such entry found"

			elif(user_type==1):
				id_get=request.POST.get("roll_no")
				print id_get
				student=students_data.objects.get(id=id_get)
				if(student!=None):
					send_sms

					mobile=student.mobile
					otp=str(random.randint(999,9999))
					send_sms(student.mobile,"Otp for the app is "+otp)
					student.otp=otp
					student.save()
					response['success']=True
					response['message']="An otp has been sent to your email:"+hide(student.email)+" and to mobile:"+hide(student.mobile)
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

@csrf_exempt
def verify(request):
	response={}
	if(request.method=='POST'):
		try:
			user_type=int(request.POST.get("login_type"))
			print "user_type",user_type
			#user_type 0 teacher
			#user_type 1 student
			if(user_type==0):
				id_get=request.POST.get("roll_no")
				print id_get
				teacher=teachers_data.objects.get(id=id_get)
				if(teacher!=None):
					if(teacher.otp==request.POST.get('otp')):
						response['success']=True
						response['message']="Access granted"
						response['access_token']=jwt.encode({'id':id_get,"user_type":user_type}, str(KEYS.objects.get(key='jwt').value), algorithm='HS256')

					else:
						response['success']=False
						response['message']="Otp did not match,Try Again"
				else:
					response['success']=False
					response['message']="No such entry found"

			elif(user_type==1):
				id_get=request.POST.get("roll_no")
				print id_get
				student=students_data.objects.get(id=id_get)
				if(student!=None):
					if(student.otp==request.POST.get('otp')):
						response['success']=True
						response['message']="Access granted"
						response['access_token']=jwt.encode({'id':id_get,"user_type":user_type}, str(KEYS.objects.get(key='jwt').value), algorithm='HS256')

					else:
						response['success']=False
						response['message']="Otp did not match,Try Again"
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
