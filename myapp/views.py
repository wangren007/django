from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request): #请求体
	return HttpResponse("sunck is a good man")  #输入127.0.0.1返回的数值
def detail(request,num1,num2):
	return HttpResponse("detail-(%s+%s)"%(num1,num2))

from .models import Grades,Students
def grades(request):
	#去模版里取数据
	gradesList=Grades.objects.all()
	#将数据传递给模版，模版在渲染页面，在将渲染好的页面返回浏览器
	return render(request,'myapp/grades.html',{"grades":gradesList})
def students(request):
	#去模版里取数据
	studentsList=Students.objects.all()
	# 将数据传递给模版，模版在渲染页面，在将渲染好的页面返回浏览器
	return render(request,'myapp/students.html',{"students":studentsList})

def gradesStudents(request,num):
	#获得对应的班级对象
	grade=Grades.objects.get(id=num)
	#获得班级下的所有学生对象列表
	studentsList=grade.students_set.all()
	return render(request,'myapp/students.html',{"students":studentsList})
