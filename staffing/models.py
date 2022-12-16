from django.db import models
from employee.models import Employee,Post,Department

from inf0_list.models import Info_list
# Create your models here.


class Staffing(models.Model):
    id_employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    id_info_list = models.ForeignKey(Info_list,on_delete=models.CASCADE)
    zp = models.PositiveIntegerField()
    hours = models.PositiveIntegerField()



class Salary(models.Model):
    id_staffing = models.ForeignKey(Staffing,on_delete=models.CASCADE)