# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0010_auto_20160129_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='child_name',
            field=models.CharField(max_length=20, help_text='please enter last name, first'),
        ),
    ]
