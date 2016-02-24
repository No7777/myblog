# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20160108_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u56de\u590d\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u6539\u65f6\u95f4'),
        ),
    ]
