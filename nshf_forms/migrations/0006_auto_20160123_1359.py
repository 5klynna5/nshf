# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0005_auto_20160123_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_childcare_county_paid',
            field=models.CharField(default='UNKNOWN', max_length=9, choices=[('ALL_PAID', 'All paid by county'), ('SOME_PAID', 'Some paid by county'), ('NONE_PAID', 'None paid by county'), ('UNKNOWN', 'Unknown')]),
        ),
    ]
