# -*- coding:utf8-*-
#author:define.zhang
#Mail:define.zhang@qq.com
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from models import Department, PublicIPAddress

def PublicIPResource(request):
    records = PublicIPAddress.objects.all()
    return render_to_response('outside-ip.html',{'records':records}) 
