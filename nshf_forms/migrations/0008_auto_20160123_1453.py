# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0007_auto_20160123_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='one_month_update',
            name='current_hourly_wage',
            field=models.DecimalField(decimal_places=2, help_text='Please write just the number of dollars client makes per hour of work, 0 if unemployed, 99.99 if unknown', max_digits=4),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_gross_income',
            field=models.DecimalField(decimal_places=2, help_text='please enter 999.99 if not known', max_digits=10),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_net_income',
            field=models.DecimalField(decimal_places=2, help_text='please enter 999.99 if not known', max_digits=10),
        ),
    ]
