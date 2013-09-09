# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class Department_level_one(models.Model):
    name = models.CharField(max_length=50,verbose_name='一级部门')
    description = models.CharField(max_length=100,verbose_name='部门描述')

    def __unicode__(self):
        return self.name

class Department_level_two(models.Model):
    name = models.CharField(max_length=50,verbose_name='二级部门')
    description = models.CharField(max_length=100,verbose_name='部门描述')
    top_level = models.ForeignKey(Department_level_one,verbose_name='上级部门')

    def __unicode__(self):
        return self.name

class WorkArea(models.Model):
    workspace = models.CharField(max_length=50,verbose_name='办公区域')
    
    def __unicode__(self):
        return self.workspace
class Service(models.Model):
    SERVICE_TYPE_CHOICE = (
            ('TCP', 'TCP协议'),
            ('UDP', 'UDP协议'),
            )
    num_port = models.CharField(max_length=5,verbose_name='端口号')
    service_type = models.CharField(max_length=10,
                                    choices=SERVICE_TYPE_CHOICE,
                                    default='TCP',verbose_name='协议类型')
    service_descr = models.CharField(max_length=50,verbose_name='协议描述')
    
    def __unicode__(self):
        return self.service_type + ':' + self.num_port

class PrivateIPAddress(models.Model):
    ipaddress = models.IPAddressField(verbose_name='内网IP')
    ip_workspace = models.ForeignKey(WorkArea, verbose_name='办公区')

    def __unicode__(self):
        return self.ipaddress

class Users(models.Model):
    username = models.CharField(max_length=15, verbose_name='用户名')
    email = models.EmailField(verbose_name='电子邮件')
    phone = models.CharField(max_length=11, verbose_name='联系电话')

    def __unicode__(self):
        return self.username


class PublicIPAddress(models.Model):
    ipaddress = models.IPAddressField(verbose_name='公网IP')
    ip_workspace = models.ForeignKey(WorkArea,verbose_name='办公区')
    ip_service_public = models.ManyToManyField(Service, verbose_name='外网服务端口')
    ip_private = models.ForeignKey(PrivateIPAddress, verbose_name='内网IP')
    ip_user = models.ManyToManyField(Users, verbose_name='使用人')

    def __unicode__(self):
        return self.ipaddress



