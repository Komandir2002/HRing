from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    Job_title = models.CharField(max_length=255)

    def __str__(self):
        return self.Job_title


class Department(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department



class Employee(models.Model):
    FIO = models.CharField(max_length=40)
    Job_title_id = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='id_job_title')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='id_department')


    def __str__(self):
        return self.FIO



class CustomUser(User):
    GENDER_TYPE = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(choices=GENDER_TYPE, max_length=100)
    phone_number = models.CharField(max_length=100)
    age = models.DateField(null=True)
