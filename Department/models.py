# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=50,verbose_name='部门名称')
    dept_descr = models.CharField(max_length=100,verbose_name='部门描述')

    def __unicode__(self):
        return self.dept_name

class PublicService(models.Model):
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

class PrivateService(models.Model):
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
    ip_address = models.IPAddressField(verbose_name='内网IP')
    ip_descr = models.CharField(max_length=100, verbose_name='备注')

    def __unicode__(self):
        return self.ip_address

class Users(models.Model):
    username = models.CharField(max_length=15, verbose_name='用户名')
    email = models.EmailField(verbose_name='电子邮件')
    phone = models.CharField(max_length=11, verbose_name='联系电话')

    def __unicode__(self):
        return self.username

class PublicIPAddress(models.Model):
    WORK_SPACE_CHOICE = (
            (u'大恒', u'大恒办公区'),
            (u'大地', u'大地办公区'),
            (u'方恒', u'方恒办公区'),
            (u'宝能', u'宝能办公区'),
            (u'昌平', u'昌平办公区'),
            (u'厦门', u'厦门办公区'),
            (u'上海', u'上海办公区'),
            (u'武汉', u'武汉办公区'),
            )
    ip_address = models.IPAddressField(verbose_name='公网IP')
    ip_service_public = models.ForeignKey(PublicService, verbose_name='外网服务端口')
    ip_private_address = models.ForeignKey(PrivateIPAddress, verbose_name='内网IP')
    ip_service_private = models.ForeignKey(PrivateService, verbose_name='内网服务端口')
    ip_user = models.ForeignKey(Users, verbose_name='使用人')
    ip_workspace = models.CharField(max_length=50,
                                verbose_name=u'办公区域',
                                choices=WORK_SPACE_CHOICE,
                                default=u'大恒')
    def __unicode__(self):
        return self.ip_address
