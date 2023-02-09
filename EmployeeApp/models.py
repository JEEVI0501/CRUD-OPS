from django.db import models

# Create your models here.

class Department(models.Model):
    DeptId = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length = 50)

class Employees(models.Model):
    EmpId = models.AutoField(primary_key=True)
    EmpName = models.CharField(max_length=50)
    Dept = models.CharField(max_length=50)
    Doj = models.DateField()
    EmpPic = models.CharField(max_length=100)