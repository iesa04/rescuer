from django.contrib import admin

from .models import UserType,Users, AdminDetail, CustomerDetail, SupplierDetail

admin.site.register(UserType)
admin.site.register(Users)
#admin.site.register(AdminDetail)
admin.site.register(CustomerDetail)
admin.site.register(SupplierDetail)
