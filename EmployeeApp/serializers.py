from rest_framework import serializers
from EmployeeApp.models import Department,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DeptId',
                  'DeptName')

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmpId',
                  'EmpName',
                  'Dept',
                  'Doj',
                  'EmpPic')