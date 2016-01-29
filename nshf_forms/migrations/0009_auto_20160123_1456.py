# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0008_auto_20160123_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='one_month_update',
            name='current_phone',
            field=models.CharField(help_text='Does client have working phone that is always on?', choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3),
        ),
    ]
