# Generated by Django 2.2.3 on 2019-08-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_manage_plat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='code',
            field=models.CharField(default='', max_length=30, verbose_name='设备代号'),
        ),
    ]
