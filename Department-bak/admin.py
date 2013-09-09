# -*- coding:utf8 -*-
from django.contrib import admin
from Department.models import Department_level_one, Department_level_two, PublicIPAddress, PrivateIPAddress, Service, Users, WorkArea


class PublicIPAddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department_level_one)
admin.site.register(Department_level_two)
admin.site.register(Service)
admin.site.register(PublicIPAddress, PublicIPAddressAdmin)
admin.site.register(PrivateIPAddress)
admin.site.register(Users)
admin.site.register(WorkArea)
