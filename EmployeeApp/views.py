from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.parsers import JSONParser
from EmployeeApp.models import Department,Employees
from EmployeeApp.serializers import DepartmentSerializer, EmpSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def deptApi(request,id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data, safe = False)
    elif request.method =='POST':
        dept_data = JSONParser().parse(request)
        deptSerializer = DepartmentSerializer(data = dept_data)
        if deptSerializer.is_valid():
            deptSerializer.save()
            return JsonResponse("Successfully Added",safe = False)
        return  JsonResponse("Couldn't ADD",safe = False)
    elif request.method == 'PUT':
        dept_data = JSONParser().parse(request)
        dept = Department.objects.get(DeptId = dept_data['DeptId'])
        dept_serializer = DepartmentSerializer(dept,dept_data)

        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse("Successfully Updated",safe = False)
        return  JsonResponse("Couldn't Update",safe = False)
    
    elif request.method =='DELETE':
        dept_data = Department.objects.get(DeptId = id)
        dept_data.delete()
        return JsonResponse("Successfully Deleted",safe = False)
    
@csrf_exempt
def employeesApi(request,id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmpSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data, safe = False)
    elif request.method =='POST':
        emp_data = JSONParser().parse(request)
        print(emp_data)
        employees_serializer = EmpSerializer(data = emp_data)
        print(employees_serializer.is_valid())
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Successfully Added",safe = False)
        return  JsonResponse("Couldn't ADD",safe = False)
    elif request.method == 'PUT':
        emp_data = JSONParser().parse(request)
        print(emp_data)
        emp = Employees.objects.get(EmpId = emp_data['EmpId'])
        employees_serializer = EmpSerializer(emp,emp_data)

        if  employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Successfully Updated",safe = False)
        return  JsonResponse("Couldn't Update",safe = False)
    
    elif request.method =='DELETE':
        emp_data = Employees.objects.get(EmpId = id)
        emp_data.delete()
        return JsonResponse("Successfully Deleted",safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)