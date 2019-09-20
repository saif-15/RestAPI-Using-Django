import json
from restapiexample.models import Student
from django.http import HttpResponse 

def is_json(data):
	validate=False
	try:
		json_data=json.loads(data)
		validate=True
	except ValueError:
		validate=False
	return validate

def get_object_by_id(self,id):
        try:
            stds = Student.objects.get(id=id)
            return stds
        except Student.DoesNotExist:
        	json_data=json.dumps({'msg':'record doesnt found'})
        	return HttpResponse(json_data,content_type='application/json')
        
