# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0011_auto_20160129_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_credit_report',
            field=models.DateField(blank=True, help_text='Approximately - when was the last time client accessed a credit report?', null=True),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_hire_date',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>', null=True),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='client_date_of_birth',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_hourly_wage',
            field=models.DecimalField(decimal_places=2, max_digits=4, help_text='Please write just the number of dollars client makes per hour of work, 0 if unemployed'),
        ),
    ]
