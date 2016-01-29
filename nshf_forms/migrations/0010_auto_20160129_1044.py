# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0009_auto_20160123_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='child_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='chemical_health_assessment',
            field=models.DateField(null=True, blank=True, help_text='please enter date assessment was completed in format yyyy-mm-dd'),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='chemical_health_completed',
            field=models.DateField(null=True, blank=True, help_text='please enter date course was completed in format yyyy-mm-dd'),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='extra_subsidy',
            field=models.CharField(default='UNKNOWN', max_length=7, choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')]),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='why_extra_subsidy',
            field=models.CharField(blank=True, max_length=9, choices=[('FINANCIAL', 'Financial'), ('SINGLE_MH', 'Single mental health'), ('GROUP_MH', 'Group mental health'), ('PARENTING', 'Parenting'), ('OTHER', 'Other')]),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='why_extra_subsidy_other',
            field=models.CharField(help_text='for what other reason did client received the extra subsidy?', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='kid',
            name='child_name',
            field=models.CharField(help_text='please enter first and last name', max_length=20),
        ),
    ]
