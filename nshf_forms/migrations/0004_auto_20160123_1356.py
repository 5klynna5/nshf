# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0003_auto_20160123_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_follow_up',
            old_name='follow_up_receiving_MFIP',
            new_name='follow_up_receiving_MFIP_Cash',
        ),
        migrations.RemoveField(
            model_name='client_follow_up',
            name='year',
        ),
        migrations.AddField(
            model_name='client_follow_up',
            name='follow_up_receiving_MFIP_Housing',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_average_hours_per_week',
            field=models.CharField(choices=[('NONE', 'None'), ('LESS_THAN_25', 'less than 25'), ('25_TO_34', '25 - 34'), ('35_PLUS', '35 +'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_bank_account',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_car',
            field=models.CharField(choices=[('NO_CAR', 'Does not own car'), ('NOT_INSURED', 'Car NOT insured'), ('INSURED', 'Car insured'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=11),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_childcare_county_paid',
            field=models.CharField(choices=[('ALL_PAID', 'All paid by county'), ('SOME_PAID', 'Some paid by county'), ('NONE_PAID', 'None paid by county'), ('UNKNONW', 'Unknown')], default='UNKNOWN', max_length=9),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_criminal_history',
            field=models.CharField(choices=[('NO', 'No'), ('MISDEM', 'Misdemeanor'), ('GROSS', 'Gross Misdemeanor'), ('FELONY', 'Felony'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_drivers_license',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_employment_sector',
            field=models.CharField(choices=[('BUSINESS_SERVICES', 'Business Services'), ('CONSTRUCTION', 'Construction'), ('CUSTOMER_SERVICE', 'Customer Service'), ('EDUCATION', 'Education'), ('FINANCIAL', 'Financial'), ('FOOD_SERVICE', 'Food Service'), ('GOVERNMENT', 'Government'), ('HEALTH_CARE', 'Health Care'), ('INFORMATION', 'Information'), ('LEISURE_HOSPITALITY', 'Leisure and Hospitality'), ('MANUFACTURING', 'Manufacturing'), ('NON_PROFIT', 'Non-profit'), ('OFFICE_ADMIN', 'Office / Administrative'), ('RETAIL', 'Retail'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], default='UNKNOWN', max_length=19),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_employment_type',
            field=models.CharField(choices=[('FULL_W_BEN', 'Full time with benefits'), ('FULL', 'Full time'), ('PART', 'Part time'), ('TEMP_FT', 'Temp full time'), ('TEMP_PT', 'Temp part time'), ('UE', 'Unemployed'), ('NOT_KNOWN', 'NOT KNOWN')], default='NOT_KNOWN', max_length=10),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_enrolled_educational',
            field=models.CharField(choices=[('NONE', 'Not enrolled'), ('GED_TUTOR', 'GED Tutor'), ('GED_CLASS', 'GED Class'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_hire_date',
            field=models.DateField(default=9801, help_text='Please use the following format: <em>YYYY-MM-DD</em>, enter 9999-99-99 if unknown'),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_hourly_wage',
            field=models.DecimalField(decimal_places=2, default=9999.99, max_digits=4, help_text='enter 9999.99 if unknown'),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_level_of_education',
            field=models.CharField(choices=[('NO_ED', 'NO High School Diploma or GED'), ('HIGH_SCHOOL', 'High School Diploma'), ('GED', 'GED'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree'), ('ADVANCED', 'Advanced Degree'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_primary_childcare_type',
            field=models.CharField(choices=[('CENTER', 'Center'), ('FAMILY', 'Family'), ('FRIENDS', 'Friends'), ('OTHER', 'Other'), ('NONE', 'None'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_WIC',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_child_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_emergency_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_energy_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_food_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_unemployment',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_relationship',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('PARTNERED', 'Partnered'), ('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('WIDOWED', 'Widowed'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=9),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='long_term_homeless',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_average_hours_per_week',
            field=models.CharField(choices=[('NONE', 'None'), ('LESS_THAN_25', 'less than 25'), ('25_TO_34', '25 - 34'), ('35_PLUS', '35 +'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=12),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_employment_type',
            field=models.CharField(choices=[('FULL_W_BEN', 'Full time with benefits'), ('FULL', 'Full time'), ('PART', 'Part time'), ('TEMP_FT', 'Temp full time'), ('TEMP_PT', 'Temp part time'), ('UE', 'Unemployed'), ('NOT_KNOWN', 'NOT KNOWN')], default='NOT_KNOWN', max_length=10),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_hourly_wage',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=4, help_text='Please write just the number of dollars client makes per hour of work, 0 if unemployed, 99.99 if unknown'),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_gross_income',
            field=models.DecimalField(decimal_places=2, default=999.99, max_digits=10, help_text='please enter 999.99 if not known'),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_net_income',
            field=models.DecimalField(decimal_places=2, default=999.99, max_digits=10, help_text='please enter 999.99 if not known'),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_phone',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=3, help_text='Does client have working phone that is always on?', default='UNKNOWN'),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_WIC',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_child_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_emergency_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_energy_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_food_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_unemployment',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
    ]
