from django.views.generic import View
from restapiexample.models import Student
from django.core.serializers import serialize
from django.http import HttpResponse
from restapiexample.utils import is_json,get_object_by_id
from restapiexample.forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentViewClass(View):

	def get(self,request,id,*args,**kwargs):
		stds = Student.objects.get(id=id)
		json_data = serialize('json',[stds,])
		dic=json.loads(json_data)
		new_list=[]
		for obj in dic:
			std=obj['fields']

			new_list.append(std)
		json_data=json.dumps(new_list)
		return HttpResponse( json_data ,content_type='application/json')

	def delete(self,request,id,*args,**kwargs):
		std=get_object_by_id(self=self,id=id)
		std.delete()
		json_data=json.dumps({'msg':'resource deleted successfully'})
		return HttpResponse(json_data,content_type='application/json')

	def put(self,request,id,*args,**kwargs):
		std=get_object_by_id(self,id)
		coming_data=request.body
		if not is_json(coming_data):
			json_data=json.dumps({'msg':'data is invalid'})
			return HttpResponse(json_data,content_type='application/json',status=400)
		original_data={
		'name':std.name,
		'father_name':std.father_name,
		'age':std.age,
		'department':std.department
		}
		coming_data=json.loads(coming_data)
		original_data.update(coming_data)
		stdform=StudentForm(original_data,instance=std)
		if stdform.is_valid:
			stdform.save(commit=True)
			json_data=json.dumps({'msg':'resource updated successfully'})
			return HttpResponse(json_data,content_type='application/json')
		if stdform.errors:
			json_data=json.dumps({'msg':'resource cant update successfully'})
			return HttpResponse(json_data,content_type='application/json',status=400)

@method_decorator(csrf_exempt,name='dispatch')
class StudentListClass(View):
	def get(self,request,*args,**kwargs):
		stds = Student.objects.all()
		json_data = serialize('json',stds)
		dic=json.loads(json_data)
		new_list=[]
		for obj in dic:
			std=obj['fields']
			new_list.append(std)
		json_data=json.dumps(new_list)
		return HttpResponse( json_data ,content_type='application/json')

	def post(self,request,*args,**kwargs):
		std=request.body
		json_is=is_json(std)
		if not json_is:
			json_data=json.dumps({'msg':'data is invalid'})
			return HttpResponse(json_data,content_type='application/json',status=400)
		std_dc=json.loads(std)

		std_form=StudentForm(std_dc)
		if std_form.is_valid():
			std_form.save(commit=True)
			json_data=json.dumps({'msg':'resource created successfully'})
			return HttpResponse(json_data,content_type='application/json',status=201)
		if std_form.errors:
			json_data=json.dumps({'msg':'resource cant created successfully'})
			return HttpResponse(json_data,content_type='application/json',status=400)
   

