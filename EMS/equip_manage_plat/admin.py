from django.contrib import admin
# from django.contrib.auth.models import Group, User as AdminUser
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from .models import Equipment
from import_export import resources
# from .resources import EquipmentResource

# Register your models here.
@admin.register(Equipment)
class EquipmentAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    list_display = ('code', 'IMEI', 'stage', 'owner', 'borrower', 'borrow_date', 'remark')
    # readonly_fields = ('book_name','author_name','total_num','available_num')
    search_fields = ('IMEI', 'code', 'borrower')
    # list_filter = ['available_num']
    list_per_page = 10
    admin.AdminSite.site_header = '设备管理平台'
    admin.AdminSite.site_title = '管理后台'


class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Equipment
        skip_unchanged = True
        import_id_fields = ['IMEI']
        fields = ('id', 'code', 'IMEI', 'stage', 'owner', 'borrower', 'borrow_date', 'remark')


# @admin.register(Borrower)
# class BorrowerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'borrow_date', 'remark')
#     list_per_page = 10

