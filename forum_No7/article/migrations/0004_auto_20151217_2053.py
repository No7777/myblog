# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20151216_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='owner',
            new_name='author',
        ),
    ]
