# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_follow_up',
            name='follow_up_city',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='client_follow_up',
            name='follow_up_housing',
            field=models.CharField(choices=[('MRKT_RATE', 'Market rate rental'), ('SECTION_8', 'Section 8'), ('OWN_HOME', 'Own home'), ('FRNDS_FAM', 'With friends or family'), ('SHELTER', 'Shelter'), ('LEAVING_TC', 'Leaving the Twin Cities'), ('PROGRAM', 'Housing program'), ('OTHER', 'Other')], max_length=9, blank=True),
        ),
    ]
