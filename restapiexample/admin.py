from django.contrib import admin
from restapiexample.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','father_name','age','department']


admin.site.register(Student,StudentAdmin)