# -*-coding:utf8-*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Department.models import Department, PublicIPAddress, PublicService, PrivateService, Users, PrivateIPAddress
import datetime

def index(request):
    #return HttpResponse('hello world!')
    #dept_one = Department.objects.all()
    num_dept = Department.objects.count() #部门数量
    num_publicipaddress = PublicIPAddress.objects.count()
    num_privateipaddress = PrivateIPAddress.objects.count()
    num_publicservice = PublicService.objects.count()
    num_privateservice = PrivateService.objects.count()
    num_users = Users.objects.count()
    now = datetime.datetime.now() #当前时间
    return render_to_response('index.html',{'num_dept':num_dept,
                                            'num_publicipaddress':num_publicipaddress,
                                            'num_privateipaddress':num_privateipaddress,
                                            'num_publicservice':num_publicservice,
                                            'num_privateservice':num_privateservice,
                                            'num_users':num_users,
                                            'current_date':now})
