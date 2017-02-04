import requests
#from splash_screen.models import keys

def send_notification(fcm,data_type,body,title="EduSmt"):
	json={}
	json['to']=str(fcm)
	notification={}
	notification['body']=str(body)
	notification['title']=str(title)
	json['notification']=notification
	data={}
	data['type']=int(data_type)
	data['title']=str(title)
	data['body']=str(body)
	json['data']=data
	print json
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	'Authorization':'key=AAAAihKlwdc:APA91bE1MdnGVDnW6Psgvm4BiCskiqxBx9YedekxPVd-G6bn0n6fFwCseDB0mWoP8ZMQHOiJyxKwMV2baciFFUsXYSkcZ3Bn-pyltMO6fuKGIDa6b37Pv3CDGOfck6mS1HktxgKaZksv'
	}
	#print json
	r=requests.post(url,headers=headers,json=json)
	for o in r:
		print "Sending fcm",o