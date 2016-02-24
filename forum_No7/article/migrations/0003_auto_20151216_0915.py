# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151215_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='owener',
            new_name='owner',
        ),
    ]
