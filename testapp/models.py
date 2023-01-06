from django.db import models

# Create your models here.
class StudentModel(models.Model):
    stu_name = models.CharField(max_length=120)
    stu_age = models.IntegerField()
    stu_city = models.CharField(max_length=120)
    stu_roll_no = models.IntegerField()

    def __str__(self):
        return self.stu_name
