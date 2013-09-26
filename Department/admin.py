# -*- coding:utf8 -*-
from django.contrib import admin
from Department.models import Department, PublicIPAddress, PrivateIPAddress, PublicService,PrivateService, Users


class PublicIPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'ip_service_public', 'ip_private_address', 'ip_service_private','ip_workspace', 'ip_user')    

class PublicServiceAdmin(admin.ModelAdmin):
    list_display = ('num_port', 'service_type', 'service_descr')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_descr')

class PrivateIPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'ip_descr')
    
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    list_filter = ('username', 'email', 'phone')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(PublicService, PublicServiceAdmin)
admin.site.register(PrivateService, PublicServiceAdmin)
admin.site.register(PublicIPAddress, PublicIPAddressAdmin)
admin.site.register(PrivateIPAddress, PrivateIPAddressAdmin)
admin.site.register(Users, UsersAdmin)
