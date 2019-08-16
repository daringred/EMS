from django.db import models


# Create your models here.
# class Borrower(models.Model):
#     # IMEI号
#     # IMEI = models.CharField(max_length=100)
#
#     # 首次借用人，设置字段的别名，显示在admin
#     name = models.CharField(u'借用人', max_length=100)
#
#     # 借用日期
#     borrow_date = models.DateTimeField(u'借用日期', auto_now_add=True)
#
#     # 备注
#     remark = models.TextField(u'备注', blank=True)
#
#     # 在admin显示外键字段的具体值而不是..object
#     def __str__(self):
#         return self.name
#
#     # 设置表的别名，显示在admin
#     class Meta:
#         verbose_name = '借用人'
#         verbose_name_plural = '借用人'


class Equipment(models.Model):
    # id = models.AutoField(primary_key='True')
    # 代号
    code = models.CharField(u'设备代号', default='', max_length=30)

    # IMEI号
    IMEI = models.CharField(default='', max_length=100)

    # 阶段
    stage = models.CharField(u'阶段', max_length=100, default='', blank=True)

    # 归属人
    owner = models.CharField(u'保管人', default='', max_length=100)

    # 借用人
    # 默认在外键所在的表中保存的是对应主表的数据行的id值,该字段名称为模型字段名+ "_id" 这里就是 user_id，django1.9后on_delete参数必不可少
    # 设置related_name后可以通过 主表.related_name.all() 查询，否则就是 equipment_set
    # null=true代表数据库里该字段可以为空， blank=true代表admin中该表单栏可以为空，显示为灰色
    # borrower = models.ForeignKey(Borrower, related_name='equips', verbose_name=u'借用人',
    #                              on_delete=models.CASCADE, null=True, blank=True)

    # 借用人
    borrower = models.CharField(u'借用人', max_length=50, default='', blank=True)

    # 借用日期
    borrow_date = models.DateTimeField(u'借用日期', null=True, blank=True)

    # 备注
    remark = models.TextField(u'备注', default='', blank=True)

    # # 文件上传
    # file_upload = models.FileField(upload_to='file', null=True)

    class Meta:
        verbose_name = u'设备'
        verbose_name_plural = u'设备'
