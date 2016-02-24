# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20151214_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
