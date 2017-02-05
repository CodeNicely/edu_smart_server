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
	#json['data']=data
	print json
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	'Authorization':'key=AAAAUmbx-w4:APA91bG500fEZL878TisrSFWtLVwLdYZYH-2GZn7jUGkJg36QkG8RN5JdNhPAtH5LrB5E4A4s3Jws2H5t63CBeZ_ymveBU8XlRdb_FwcVfc_KgMyxi7SQ6AUl_YeY2tf2e2jtP0Qob-Z'
	}
	#print json
	r=requests.post(url,headers=headers,json=json)
	for o in r:
		print "Sending fcm",o