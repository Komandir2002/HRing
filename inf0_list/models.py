from django.db import models
from employee.models import Employee

CHOISE_INFO = (
    ("Болеет","Болеет"),
    ("Командировке","Командировке"),
    ("Работает","Работает"),
)

class Info_list(models.Model):
    Employe = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='info_list')
    information = models.CharField(choices=CHOISE_INFO,max_length=20)


    def __str__(self):
        return self.information
