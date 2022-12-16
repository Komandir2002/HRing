from django.db import models
from employee.models import Employee
from employee.models import Employee,Department
# Create your models here.



class Reference_table(models.Model):
    FIO = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Salary = models.PositiveIntegerField()