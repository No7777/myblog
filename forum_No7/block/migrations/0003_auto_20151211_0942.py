# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20151211_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='block_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='admin_name',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='block_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='block',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u6539\u65f6\u95f4'),
        ),
    ]
