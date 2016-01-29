# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0004_auto_20160123_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_hire_date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>, enter 9999-99-99 if unknown'),
        ),
    ]
