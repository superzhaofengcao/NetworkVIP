# -*- coding:utf8 -*-
from django.contrib import admin
from Department.models import Department, PublicIPAddress, PrivateIPAddress, PublicService,PrivateService, Users


class PublicIPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'ip_service_public', 'ip_private_address', 'ip_service_private','ip_workspace', 'ip_user')    

class PublicServiceAdmin(admin.ModelAdmin):
    list_display = ('num_port', 'service_type', 'service_descr')

admin.site.register(Department)
admin.site.register(PublicService, PublicServiceAdmin)
admin.site.register(PrivateService, PublicServiceAdmin)
admin.site.register(PublicIPAddress, PublicIPAddressAdmin)
admin.site.register(PrivateIPAddress)
admin.site.register(Users)
