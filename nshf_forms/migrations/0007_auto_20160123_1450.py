# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0006_auto_20160123_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_hourly_wage',
            field=models.DecimalField(decimal_places=2, max_digits=4, help_text='enter 9999.99 if unknown'),
        ),
    ]
