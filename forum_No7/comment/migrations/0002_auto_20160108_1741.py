# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u666e\u901a'), (-1, '\u5220\u9664')]),
        ),
    ]
