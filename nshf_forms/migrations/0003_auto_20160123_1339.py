# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nshf_forms', '0002_auto_20160122_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_follow_up',
            old_name='follow_up_progress',
            new_name='follow_up_other_progress',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_amount_in_bank',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_average_hours_per_week',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_bank_account',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_car',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_childcare_county_paid',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_children',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_contact',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_credit_report',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_credit_score',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_drivers_license',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_employment_sector',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_employment_type',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_enrolled_educational',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_hourly_wage',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_job_hire_date',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_level_of_education',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_monthly_gross_income',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_partner_client',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_phone',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_primary_childcare_type',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_MFIP',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_WIC',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_child_support',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_emergency_assistance',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_energy_assistance',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_food_support',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_receiving_unemployment',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='exit_relationship',
        ),
        migrations.RemoveField(
            model_name='client_exit',
            name='sector_write_in',
        ),
        migrations.RemoveField(
            model_name='client_follow_up',
            name='follow_up_city',
        ),
        migrations.RemoveField(
            model_name='client_intake',
            name='baseline_receiving_MFIP',
        ),
        migrations.RemoveField(
            model_name='one_month_update',
            name='current_receiving_MFIP',
        ),
        migrations.RemoveField(
            model_name='one_month_update',
            name='current_total_debt',
        ),
        migrations.RemoveField(
            model_name='one_month_update',
            name='month',
        ),
        migrations.AddField(
            model_name='client_exit',
            name='exit_contacts',
            field=models.TextField(help_text='Best phone number to reach client in the future', blank=True),
        ),
        migrations.AddField(
            model_name='client_exit',
            name='family_friend_behavior',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_exit',
            name='leaving_the_twin_cities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_exit',
            name='partner_behavior',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_follow_up',
            name='enrolled_other_text',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='client_intake',
            name='baseline_drivers_permit',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='client_intake',
            name='baseline_receiving_MFIP_Cash',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='client_intake',
            name='baseline_receiving_MFIP_Housing',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='current_receiving_MFIP_Cash',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='current_receiving_MFIP_Housing',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='debt_paid_this_month',
            field=models.DecimalField(help_text='please enter the number of dollars of debt paid this month', max_digits=10, null=True, blank=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='one_month_update',
            name='drivers_permit',
            field=models.DateField(help_text='If client got drivers permit, please enter date here', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client_exit',
            name='exit_total_debt',
            field=models.DecimalField(help_text='Total estimated client debt, or sum of above debt', max_digits=10, null=True, blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='client_follow_up',
            name='follow_up_enrolled_educational',
            field=models.CharField(choices=[('NONE', 'Not enrolled'), ('GED_TUTOR', 'GED Tutor'), ('GED_CLASS', 'GED Class'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree'), ('ADVANCED', 'Advanced Degree'), ('OTHER', 'Other')], help_text='Is client currently enrolled in educational program?', max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_average_hours_per_week',
            field=models.CharField(choices=[('NONE', 'None'), ('LESS_THAN_25', 'less than 25'), ('25_TO_34', '25 - 34'), ('35_PLUS', '35 +'), ('UNKNOWN', 'Unknown')], help_text='enter 9999.99 if unknown', max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_bank_account',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_car',
            field=models.CharField(choices=[('NO_CAR', 'Does not own car'), ('NOT_INSURED', 'Car NOT insured'), ('INSURED', 'Car insured'), ('UNKNOWN', 'Unknown')], max_length=11),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_childcare_county_paid',
            field=models.CharField(choices=[('ALL_PAID', 'All paid by county'), ('SOME_PAID', 'Some paid by county'), ('NONE_PAID', 'None paid by county'), ('UNKNONW', 'Unknown')], max_length=9),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_criminal_history',
            field=models.CharField(choices=[('NO', 'No'), ('MISDEM', 'Misdemeanor'), ('GROSS', 'Gross Misdemeanor'), ('FELONY', 'Felony'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_drivers_license',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_employment_sector',
            field=models.CharField(choices=[('BUSINESS_SERVICES', 'Business Services'), ('CONSTRUCTION', 'Construction'), ('CUSTOMER_SERVICE', 'Customer Service'), ('EDUCATION', 'Education'), ('FINANCIAL', 'Financial'), ('FOOD_SERVICE', 'Food Service'), ('GOVERNMENT', 'Government'), ('HEALTH_CARE', 'Health Care'), ('INFORMATION', 'Information'), ('LEISURE_HOSPITALITY', 'Leisure and Hospitality'), ('MANUFACTURING', 'Manufacturing'), ('NON_PROFIT', 'Non-profit'), ('OFFICE_ADMIN', 'Office / Administrative'), ('RETAIL', 'Retail'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], help_text='enter 9999-99-99 if unknown', max_length=19),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_employment_type',
            field=models.CharField(choices=[('FULL_W_BEN', 'Full time with benefits'), ('FULL', 'Full time'), ('PART', 'Part time'), ('TEMP_FT', 'Temp full time'), ('TEMP_PT', 'Temp part time'), ('UE', 'Unemployed'), ('NOT_KNOWN', 'NOT KNOWN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_enrolled_educational',
            field=models.CharField(choices=[('NONE', 'Not enrolled'), ('GED_TUTOR', 'GED Tutor'), ('GED_CLASS', 'GED Class'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree'), ('UNKNOWN', 'Unknown')], max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_level_of_education',
            field=models.CharField(choices=[('NO_ED', 'NO High School Diploma or GED'), ('HIGH_SCHOOL', 'High School Diploma'), ('GED', 'GED'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree'), ('ADVANCED', 'Advanced Degree'), ('UNKNOWN', 'Unknown')], max_length=12),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_primary_childcare_type',
            field=models.CharField(choices=[('CENTER', 'Center'), ('FAMILY', 'Family'), ('FRIENDS', 'Friends'), ('OTHER', 'Other'), ('NONE', 'None'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_WIC',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_child_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_emergency_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_energy_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_food_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_receiving_unemployment',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='baseline_relationship',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('PARTNERED', 'Partnered'), ('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('WIDOWED', 'Widowed'), ('UNKNOWN', 'Unknown')], max_length=9),
        ),
        migrations.AlterField(
            model_name='client_intake',
            name='long_term_homeless',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_average_hours_per_week',
            field=models.CharField(choices=[('NONE', 'None'), ('LESS_THAN_25', 'less than 25'), ('25_TO_34', '25 - 34'), ('35_PLUS', '35 +'), ('UNKNOWN', 'Unknown')], max_length=12),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_childcare_county_paid',
            field=models.CharField(choices=[('ALL_PAID', 'All paid by county'), ('SOME_PAID', 'Some paid by county'), ('NONE_PAID', 'None paid by county')], max_length=9, blank=True),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_employment_type',
            field=models.CharField(choices=[('FULL_W_BEN', 'Full time with benefits'), ('FULL', 'Full time'), ('PART', 'Part time'), ('TEMP_FT', 'Temp full time'), ('TEMP_PT', 'Temp part time'), ('UE', 'Unemployed'), ('NOT_KNOWN', 'NOT KNOWN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_enrolled_educational',
            field=models.CharField(choices=[('NONE', 'Not enrolled'), ('GED_TUTOR', 'GED Tutor'), ('GED_CLASS', 'GED Class'), ('TECHNICAL', 'Technical Degree or Certification'), ('ASSOCIATES', 'Associates Degree'), ('BACHELORS', 'Bachelors Degree')], help_text='Is client currently enrolled in an educational program?', max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_hourly_wage',
            field=models.DecimalField(help_text='Please write just the number of dollars client makes per hour of work, 0 if unemployed, 99.99 if unknown', max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_gross_income',
            field=models.DecimalField(help_text='please enter 999.99 if not known', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_monthly_net_income',
            field=models.DecimalField(help_text='please enter 999.99 if not known', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_phone',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], help_text='Does client have working phone that is always on?', max_length=3),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_WIC',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_child_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_emergency_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_energy_assistance',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_food_support',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='current_receiving_unemployment',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('UNKNOWN', 'Unknown')], max_length=7),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='date_form_completed',
            field=models.DateField(help_text='date form completed with client, please use format yyyy-mm-dd'),
        ),
        migrations.AlterField(
            model_name='one_month_update',
            name='other_progress',
            field=models.TextField(help_text='What other progress has client made since being in this program?', blank=True),
        ),
    ]
