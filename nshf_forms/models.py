from django.db import models
from django.utils import timezone
from django.forms import widgets

class Kid(models.Model):
    child_name = models.CharField(max_length=20, help_text = 'please enter last name, first')
    child_dob = models.DateField(blank=True, null=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    child_school = models.CharField(max_length=30, blank=True)
    child_comments = models.TextField(blank=True)


    created_date = models.DateTimeField(
            default=timezone.now)
    updated = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return self.child_name

class Client_intake(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_date_of_birth = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", null=True, blank=True)
    client_first_name = models.CharField(max_length=20)
    client_last_name = models.CharField(max_length=20)
    client_move_in = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    female = models.BooleanField(default=False)
    male = models.BooleanField(default=False)
    transgender = models.BooleanField(default=False)
    another_gender = models.BooleanField(default=False)
    gender_prefer_not_to_say = models.BooleanField(default=False)
    gender_write_in = models.CharField(max_length=200, blank=True)
    
    black_african_american = models.BooleanField(default=False)
    indigenous_native_american = models.BooleanField(default=False)
    white = models.BooleanField(default=False)
    hispanic_latino = models.BooleanField(default = False)
    asian_pacific_islander = models.BooleanField(default = False)
    multi_racial = models.BooleanField(default=False)
    another_race_ethnicity = models.BooleanField(default=False)
    race_prefer_not_to_say = models.BooleanField(default=False)
    race_write_in = models.CharField(max_length=100, blank=True)

    YES_NO_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('UNKNOWN', 'Unknown'),
    )
    
    long_term_homeless = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')

    RELATIONSHIP_CHOICES = (
        ('SINGLE', 'Single'),
        ('PARTNERED', 'Partnered'),
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
        ('UNKNOWN', 'Unknown'),
    )
    baseline_relationship = models.CharField(max_length=9, choices=RELATIONSHIP_CHOICES, default='UNKNOWN')

    baseline_partner_client = models.ManyToManyField('self', related_name='+', blank=True)

    children = models.ManyToManyField('Kid', blank = True)

    CHILDCARE_PAID_CHOICES = (
        ('ALL_PAID', 'All paid by county'),
        ('SOME_PAID', 'Some paid by county'),
        ('NONE_PAID', 'None paid by county'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_childcare_county_paid = models.CharField(max_length=9, choices=CHILDCARE_PAID_CHOICES, default='UNKNOWN')

    CHILDCARE_CHOICES = (
        ('CENTER', 'Center'),
        ('FAMILY', 'Family'),
        ('FRIENDS', 'Friends'),
        ('OTHER', 'Other'),
        ('NONE', 'None'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_primary_childcare_type = models.CharField(max_length=7, choices=CHILDCARE_CHOICES, default='UNKNOWN')

    EDUCATION_CHOICES = (
        ('NO_ED','NO High School Diploma or GED'),
        ('HIGH_SCHOOL', 'High School Diploma'),
        ('GED','GED'),
        ('TECHNICAL','Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS','Bachelors Degree'),
        ('ADVANCED','Advanced Degree'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_level_of_education = models.CharField(max_length=12, choices=EDUCATION_CHOICES, default='UNKNOWN')

    ENROLLED_CHOICES = (
        ('NONE', 'Not enrolled'),
        ('GED_TUTOR', 'GED Tutor'),
        ('GED_CLASS', 'GED Class'),
        ('TECHNICAL', 'Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS', 'Bachelors Degree'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_enrolled_educational = models.CharField(max_length=12, choices = ENROLLED_CHOICES, default='UNKNOWN')

    CRIMINAL_CHOICES = (
        ('NO', 'No'),
        ('MISDEM', 'Misdemeanor'),
        ('GROSS', 'Gross Misdemeanor'),
        ('FELONY', 'Felony'),
        ('UNKNOWN', 'Unknown')
    )
    
    baseline_criminal_history = models.CharField(max_length=7, choices = CRIMINAL_CHOICES, default='UNKNOWN')
    
    EMPLOYMENT_TYPE_CHOICES = (
        ('FULL_W_BEN', 'Full time with benefits'),
        ('FULL','Full time'),
        ('PART', 'Part time'),
        ('TEMP_FT','Temp full time'),
        ('TEMP_PT', 'Temp part time'),
        ('UE', 'Unemployed'),
        ('NOT_KNOWN', 'NOT KNOWN'),
    )

    baseline_employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES, default='NOT_KNOWN')

    SECTOR_CHOICES = (
        ('BUSINESS_SERVICES', 'Business Services'),
        ('CONSTRUCTION', 'Construction'),
        ('CUSTOMER_SERVICE', 'Customer Service'),
        ('EDUCATION', 'Education'),
        ('FINANCIAL', 'Financial'),
        ('FOOD_SERVICE', 'Food Service'),
        ('GOVERNMENT', 'Government'),
        ('HEALTH_CARE', 'Health Care'),
        ('INFORMATION', 'Information'),
        ('LEISURE_HOSPITALITY', 'Leisure and Hospitality'),
        ('MANUFACTURING', 'Manufacturing'),
        ('NON_PROFIT', 'Non-profit'),
        ('OFFICE_ADMIN', 'Office / Administrative'),
        ('RETAIL', 'Retail'),
        ('UNKNOWN', 'Unknown'),
        ('OTHER', 'Other'),
    )

    baseline_employment_sector = models.CharField(max_length=19, choices=SECTOR_CHOICES, default='UNKNOWN')

    sector_write_in = models.CharField(max_length=20, blank=True)

    baseline_hire_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>", null=True, blank=True)

    HOURS_CHOICES = (
        ('NONE', 'None'),
        ('LESS_THAN_25', 'less than 25'),
        ('25_TO_34', '25 - 34'),
        ('35_PLUS', '35 +'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_average_hours_per_week = models.CharField(max_length=12, choices = HOURS_CHOICES, default='UNKNOWN')

    baseline_hourly_wage = models.DecimalField(max_digits=4, decimal_places=2, help_text = 'enter 9999.99 if unknown')

    baseline_monthly_gross_income = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    baseline_monthly_net_income = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    baseline_credit_report = models.DateField(blank=True, null=True, help_text = 'Approximately - when was the last time client accessed a credit report?')

    baseline_credit_score = models.IntegerField(blank=True, null=True)

    credit_card_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    medical_bill_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    car_loan_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    student_loan_debt = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank = True)
    legal_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    utilities_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    cell_phone_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    pay_day_loan_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    other_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    other_debt_write_in = models.CharField(max_length=30, help_text='What other kinds of debt does the client have?',blank=True)

    baseline_total_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text = 'Total estimated client debt, or sum of above debt')

    baseline_receiving_MFIP_Cash = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_MFIP_Housing = models.CharField(max_length=7, choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_WIC = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_child_support = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_unemployment = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_food_support = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_emergency_assistance = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    baseline_receiving_energy_assistance = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
   
    baseline_bank_account = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')

    baseline_amount_in_bank = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    
    baseline_drivers_license = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')

    baseline_drivers_permit = models.CharField(max_length=7, choices=YES_NO_CHOICES, default= 'UNKNOWN')

    CAR_CHOICES = (
        ('NO_CAR', 'Does not own car'),
        ('NOT_INSURED', 'Car NOT insured'),
        ('INSURED', 'Car insured'),
        ('UNKNOWN', 'Unknown'),
    )

    baseline_car = models.CharField(max_length=11, choices=CAR_CHOICES, default = 'UNKNOWN')

    baseline_goals = models.TextField(blank=True, help_text = 'Where does client want to be in five years?')

    created_date = models.DateTimeField(
            default=timezone.now)
    updated = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return (self.client_last_name) + ', ' + (self.client_first_name) + " | " + str(self.client_id)


class One_month_update(models.Model):
    client = models.ForeignKey('Client_intake')


    date_form_completed = models.DateField(help_text='date form completed with client, please use format yyyy-mm-dd')


    RELATIONSHIP_CHOICES = (
        ('SINGLE', 'Single'),
        ('PARTNERED', 'Partnered'),
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
    )
    
    current_relationship = models.CharField(max_length=9, choices=RELATIONSHIP_CHOICES, blank=True)

    current_partner_client = models.ForeignKey('Client_intake', related_name='+', blank=True, null=True)

    new_children = models.ManyToManyField('Kid', blank = True)
    
    CHILDCARE_PAID_CHOICES = (
        ('ALL_PAID', 'All paid by county'),
        ('SOME_PAID', 'Some paid by county'),
        ('NONE_PAID', 'None paid by county'),
    )

    current_childcare_county_paid = models.CharField(max_length=9, choices=CHILDCARE_PAID_CHOICES, blank=True)

    CHILDCARE_CHOICES = (
        ('CENTER', 'Center'),
        ('FAMILY', 'Family'),
        ('FRIENDS', 'Friends'),
        ('OTHER', 'Other'),
        ('NONE', 'None'),
    )

    current_primary_childcare_type = models.CharField(max_length=7, choices=CHILDCARE_CHOICES, blank=True)
    
    EDUCATION_CHOICES = (
        ('NO_ED','NO High School Diploma or GED'),
        ('HIGH_SCHOOL', 'High School Diploma'),
        ('GED','GED'),
        ('TECHNICAL','Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS','Bachelors Degree'),
        ('ADVANCED','Advanced Degree'),
    )

    current_level_of_education = models.CharField(max_length=12, choices=EDUCATION_CHOICES, blank=True)

    ENROLLED_CHOICES = (
        ('NONE', 'Not enrolled'),
        ('GED_TUTOR', 'GED Tutor'),
        ('GED_CLASS', 'GED Class'),
        ('TECHNICAL', 'Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS', 'Bachelors Degree'),
    )

    current_enrolled_educational = models.CharField(max_length=12, choices=ENROLLED_CHOICES, blank=True, help_text = 'Is client currently enrolled in an educational program?')

    financial_education = models.DateField(blank=True, null=True, help_text = 'If completed financial education course, please enter date completed')

    ged_completed = models.DateField(blank=True, null=True, help_text = 'If completed GED, please enter date completed')

    drivers_license = models.DateField(blank=True, null=True, help_text = 'If client got drivers license, please enter date here')

    drivers_permit = models.DateField(blank=True, null=True, help_text = 'If client got drivers permit, please enter date here')

    EMPLOYMENT_TYPE_CHOICES = (
        ('FULL_W_BEN', 'Full time with benefits'),
        ('FULL','Full time'),
        ('PART', 'Part time'),
        ('TEMP_FT','Temp full time'),
        ('TEMP_PT', 'Temp part time'),
        ('UE', 'Unemployed'),
        ('NOT_KNOWN', 'NOT KNOWN'),
    )
    
    current_employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES, default='NOT_KNOWN')

    SECTOR_CHOICES = (
        ('BUSINESS_SERVICES', 'Business Services'),
        ('CONSTRUCTION', 'Construction'),
        ('CUSTOMER_SERVICE', 'Customer Service'),
        ('EDUCATION', 'Education'),
        ('FINANCIAL', 'Financial'),
        ('FOOD_SERVICE', 'Food Service'),
        ('GOVERNMENT', 'Government'),
        ('HEALTH_CARE', 'Health Care'),
        ('INFORMATION', 'Information'),
        ('LEISURE_HOSPITALITY', 'Leisure and Hospitality'),
        ('MANUFACTURING', 'Manufacturing'),
        ('NON_PROFIT', 'Non-profit'),
        ('OFFICE_ADMIN', 'Office / Administrative'),
        ('RETAIL', 'Retail'),
        ('OTHER', 'Other'),
    )

    current_employment_sector = models.CharField(max_length=19, choices=SECTOR_CHOICES, blank=True)

    sector_write_in = models.CharField(max_length=20, blank=True)

    new_hire_date = models.DateField(blank=True, null=True, help_text= 'If client has started a new job, please enter the hire date')

    job_end_date = models.DateField(blank=True, null=True, help_text = 'If client has stopped working at a job, please enter the date that job ended.')

    LEAVING_JOB_CHOICES = (
        ('QUIT', 'Quit'),
        ('FIRED', 'Fired'),
        ('LAID_OFF', 'Laid off'),
        ('NEW_JOB', 'Got another job'),
        ('OTHER', 'Other'),
    )

    reason_leaving_job = models.CharField(max_length=6, choices = LEAVING_JOB_CHOICES, blank=True, null=True, help_text='If client is leaving job, what is the reason?')
    reason_leaving_job_text = models.CharField(max_length = 40, blank=True)

    HOURS_CHOICES = (
        ('NONE', 'None'),
        ('LESS_THAN_25', 'less than 25'),
        ('25_TO_34', '25 - 34'),
        ('35_PLUS', '35 +'),
        ('UNKNOWN', 'Unknown'),
    )

    current_average_hours_per_week = models.CharField(max_length=12, choices = HOURS_CHOICES, default='UNKNOWN')

    current_hourly_wage = models.DecimalField(max_digits=4, decimal_places=2, help_text='Please write just the number of dollars client makes per hour of work, 0 if unemployed')

    current_monthly_gross_income = models.DecimalField(max_digits=10, decimal_places=2, help_text='please enter 999.99 if not known')

    current_monthly_net_income = models.DecimalField(max_digits=10, decimal_places=2, help_text='please enter 999.99 if not known')

    current_credit_report = models.DateField(blank=True, null=True, help_text = 'Most recent date client accessed credit report.')

    current_credit_score = models.IntegerField(blank=True, null=True, help_text = 'Please enter most recent known client credit score.')

    debt_paid_this_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text = 'please enter the number of dollars of debt paid this month')

    YES_NO_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('UNKNOWN', 'Unknown'),
    )

    current_receiving_MFIP_Cash = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_MFIP_Housing = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_WIC = models.CharField(max_length=7,choices=YES_NO_CHOICES,default='UNKNOWN')
    current_receiving_child_support = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_unemployment = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_food_support = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_emergency_assistance = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')
    current_receiving_energy_assistance = models.CharField(max_length=7,choices=YES_NO_CHOICES, default='UNKNOWN')

    YES_NO_ONLY_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )

    current_bank_account = models.CharField(max_length=3,choices=YES_NO_ONLY_CHOICES, blank=True)

    current_amount_in_bank = models.DecimalField(max_digits=10,decimal_places=2,help_text='Please write the amount of dollars client has in bank account.', null=True, blank=True)

    CAR_CHOICES = (
        ('NO_CAR', 'Does not own car'),
        ('NOT_INSURED', 'Car NOT insured'),
        ('INSURED', 'Car insured'),
    )
    
    current_car = models.CharField(max_length=11, choices=CAR_CHOICES, blank=True, help_text='Does client currently own a car, if so is it insured?')

    
    current_phone = models.CharField(max_length=3,choices=YES_NO_ONLY_CHOICES, help_text = 'Does client have working phone that is always on?')

    RENT_CHOICES = (
        ('ON_TIME', 'On time'),
        ('LATE', 'Late'),
        ('NOT_PAID', 'Not Paid'),
    )

    rent_paid = models.CharField(max_length=8,choices=RENT_CHOICES)

    SUBSIDY_CHOICES = (
        ('FULL', 'Full Subsidy'),
        ('PART', 'Partial Subsidy'),
        ('NO', 'No Subsidy'),
    )

    subsidy = models.CharField(max_length=4, choices = SUBSIDY_CHOICES)

    extra_subsidy = models.CharField(max_length=7, choices=YES_NO_CHOICES, default='UNKNOWN')

    EXTRA_SUBSIDY_CHOICES = (
        ('FINANCIAL', 'Financial'),
        ('SINGLE_MH', 'Single mental health'),
        ('GROUP_MH', 'Group mental health'),
        ('PARENTING', 'Parenting'),
        ('OTHER', 'Other'),
    )

    why_extra_subsidy = models.CharField(max_length=9, choices=EXTRA_SUBSIDY_CHOICES, blank=True)

    why_extra_subsidy_other = models.CharField(max_length=30, blank=True, help_text = 'for what other reason did client received the extra subsidy?')


    utilities_paid_on_time = models.CharField(max_length=3, choices=YES_NO_ONLY_CHOICES, blank=True, help_text = 'Did client pay utilities on time this month?')
    
    other_bills_paid_on_time = models.CharField(max_length=3, choices=YES_NO_ONLY_CHOICES, blank=True, help_text = 'Did client pay all other bills on time this month?')
    
    county_paperwork_submitted_on_time = models.CharField(max_length=3, choices=YES_NO_ONLY_CHOICES, blank=True, help_text = 'Did client turn in county paperwork on time this month?')

    chemical_health_assessment = models.DateField(blank=True, null=True, help_text = 'please enter date assessment was completed in format yyyy-mm-dd')

    chemical_health_completed = models.DateField(blank=True, null=True, help_text = 'please enter date course was completed in format yyyy-mm-dd')

    chemical_dependency = models.BooleanField(default=False, help_text='Has client disclosed a chemical dependency issue this month?')
    
    mental_health_assessment = models.DateField(blank=True, null=True, help_text='please enter the date client did mental health assessment in format yyyy-mm-dd')

    diagnosis = models.TextField(blank=True, help_text = 'If client has one or more mental health diagnoses, please enter here')

    other_progress = models.TextField(blank = True, help_text = 'What other progress has client made since being in this program?')

    created_date = models.DateTimeField(
            default=timezone.now)
    updated = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        month_update = str(self.date_form_completed)+" "+str(self.client)
        return month_update

class Client_exit(models.Model):

    client = models.ForeignKey('Client_intake')

    move_out_date = models.DateField(blank=True, null=True, help_text='What date is client moving out of the NSHF program?')

    completed_program = models.BooleanField(default=False, help_text='For what reasons is client leaving the program?')
    wants_to_leave = models.BooleanField(default=False)
    non_payment_of_rent = models.BooleanField(default=False)
    no_employment = models.BooleanField(default=False)
    drug_alcohol_problem = models.BooleanField(default=False)
    leaving_the_twin_cities = models.BooleanField(default=False)
    partner_behavior = models.BooleanField(default=False)
    family_friend_behavior = models.BooleanField(default=False)
    exit_reason_other = models.BooleanField(default=False)

    exit_reason_other_text = models.TextField(blank=True, null=True, help_text='for what other reason is client leaving?')

    
    credit_card_debt = models.DecimalField(max_digits=10, decimal_places=2, help_text='Please write just the number of dollars client estimates they are in debt.', null=True, blank = True)
    medical_bill_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    car_loan_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    student_loan_debt = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank = True)
    legal_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    utilities_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    cell_phone_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    pay_day_loan_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    other_debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank = True)
    other_debt_write_in = models.CharField(max_length=30, help_text='What other kinds of debt does the client have?',blank=True)

    exit_total_debt = models.DecimalField(max_digits=10, decimal_places=2, help_text = 'Total estimated client debt, or sum of above debt', blank=True, null=True)
    
    exit_contacts = models.TextField(blank=True, help_text='Best phone number to reach client in the future')

    next_address = models.TextField(blank=True, null=True, help_text='Where will client be living next? Please record address or name of program, building, etc.')

    what_worked = models.TextField(blank=True, help_text = 'What about this program worked well for you?')

    program_changes = models.TextField(blank=True, help_text='What do you think should change about this program?')

    greatest_success = models.TextField(blank=True, help_text = "what does client see as their greatest success while in this program?")

    created_date = models.DateTimeField(
            default=timezone.now)
    updated = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return "Exit: " + str(self.client)

class Client_follow_up(models.Model):

    client = models.ForeignKey('Client_intake')

    date_follow_up = models.DateField()

    EDUCATION_CHOICES = (
        ('NO_ED','NO High School Diploma or GED'),
        ('HIGH_SCHOOL', 'High School Diploma'),
        ('GED','GED'),
        ('TECHNICAL','Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS','Bachelors Degree'),
        ('ADVANCED','Advanced Degree'),
    )

    follow_up_level_of_education = models.CharField(max_length=12, choices=EDUCATION_CHOICES, blank=True)

    ENROLLED_CHOICES = (
        ('NONE', 'Not enrolled'),
        ('GED_TUTOR', 'GED Tutor'),
        ('GED_CLASS', 'GED Class'),
        ('TECHNICAL', 'Technical Degree or Certification'),
        ('ASSOCIATES', 'Associates Degree'),
        ('BACHELORS', 'Bachelors Degree'),
        ('ADVANCED', 'Advanced Degree'),
        ('OTHER', 'Other'),
    )

    follow_up_enrolled_educational = models.CharField(max_length=12, choices = ENROLLED_CHOICES, blank=True, help_text = 'Is client currently enrolled in educational program?')
    
    enrolled_other_text = models.CharField(max_length=40, blank=True)

    EMPLOYMENT_TYPE_CHOICES = (
        ('FULL_W_BEN', 'Full time with benefits'),
        ('FULL','Full time'),
        ('PART', 'Part time'),
        ('TEMP_FT', 'Temp full time'),
        ('TEMP_PT','Temp part time'),
        ('UE', 'Unemployed'),
    )
    
    follow_up_employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES, blank=True)

    SECTOR_CHOICES = (
        ('BUSINESS_SERVICES', 'Business Services'),
        ('CONSTRUCTION', 'Construction'),
        ('CUSTOMER_SERVICE', 'Customer Service'),
        ('EDUCATION', 'Education'),
        ('FINANCIAL', 'Financial'),
        ('FOOD_SERVICE', 'Food Service'),
        ('GOVERNMENT', 'Government'),
        ('HEALTH_CARE', 'Health Care'),
        ('INFORMATION', 'Information'),
        ('LEISURE_HOSPITALITY', 'Leisure and Hospitality'),
        ('NON_PROFIT', 'Non-profit'),
        ('MANUFACTURING', 'Manufacturing'),
        ('OFFICE_ADMIN', 'Office / Administrative'),
        ('RETAIL', 'Retail'),
        ('OTHER', 'Other'),
    )

    follow_up_employment_sector = models.CharField(max_length=19, choices=SECTOR_CHOICES, blank=True)
    follow_up_sector_write_in = models.CharField(max_length=20, blank=True)

    YES_NO_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )

    follow_up_receiving_MFIP_Cash = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_MFIP_Housing = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_WIC = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_child_support = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_unemployment = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_food_support = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_emergency_assistance = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)
    follow_up_receiving_energy_assistance = models.CharField(max_length=3,choices=YES_NO_CHOICES, blank=True)

    HOUSING_CHOICES = (
        ('MRKT_RATE', 'Market rate rental'),
        ('SECTION_8', 'Section 8'),
        ('OWN_HOME', 'Own home'),
        ('FRNDS_FAM', 'With friends or family'),
        ('SHELTER', 'Shelter'),
        ('LEAVING_TC', 'Leaving the Twin Cities'),
        ('PROGRAM', 'Housing program'),
        ('OTHER', 'Other'),
    )

    follow_up_housing = models.CharField(max_length=9, choices=HOUSING_CHOICES, blank=True)

    follow_up_total_debt = models.DecimalField(max_digits=10, decimal_places = 2, null=True, blank=True)

    follow_up_other_progress = models.TextField(blank=True, help_text = 'What other progress has client made since leaving the program?')

    def update(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return str(self.date_follow_up) + ' follow up ' + str(self.client)
