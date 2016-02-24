# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='admin_name',
            field=models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_desc',
            field=models.CharField(max_length=100, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_name',
            field=models.CharField(max_length=50, verbose_name='\u540d\u5b57'),
        ),
    ]
