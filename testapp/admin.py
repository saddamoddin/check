from django.contrib import admin
from testapp.models import StudentModel

# Register your models here.
class adminview(admin.ModelAdmin):
    list_display = ['stu_name','stu_roll_no','stu_city','stu_age']

admin.site.register(StudentModel,adminview)