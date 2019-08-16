from import_export import resources
from .models import Equipment


class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Equipment
        skip_unchanged = True
        import_id_fields = ['IMEI']
        fields = ('id', 'code', 'IMEI', 'stage', 'owner', 'borrower', 'borrow_date', 'remark')
