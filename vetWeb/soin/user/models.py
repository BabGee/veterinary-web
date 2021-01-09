from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	is_vet_officer = models.BooleanField(default=False)
	is_farmer = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(null=True, blank=True)
	phone_number = models.CharField(max_length=10)
	
class Vet_Officer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	kvb_number = models.IntegerField(unique=True, null=True, blank=True)

	def __str__(self):
		return f'Name: {self.user.username} KVB number {self.kvb_number}'
	
class Farmer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	location = models.CharField(max_length=100, default='My location')

	def __str__(self):
		return f'Name: {self.user.username} Phone number {self.user.phone_number}'
	
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	student_number = models.CharField(max_length=50, unique=True)
	college_name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return f'Name: {self.user.username} student number {self.student_number}'

class Farm(models.Model):
	farm_name = models.CharField(max_length=100)
	farm_owner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)

	def __str__(self):
		return f'Farm Name: {self.farm_name}'


SPECIES_CHOICES = (
    ('0', 'cattle'),
    ('1', 'sheep'),
	('2', 'goat'),
	('3', 'donkey'),
	('4', 'dog'),
	('5', 'horse'),
	('6', 'poultry'),
	('7','others')
)

DISEASE_CHOICES = (
	('A','acute'),
	('S','sub_acute')

)

DIAGNOSIS_CHOICES = (
	('C','clinical_signs'),
	('L','laboratory')
)

PROGNOSIS_CHOICES=(
	('G','good'),
	('F','fair'),
	('P','poor')
)


YES_NO_CHOICES = (
	('Y','yes'),
	('N','no')
)


class Vet_Forms(models.Model):
	is_sick_approach_form = models.BooleanField(default=False)
	is_dead_approach_form= models.BooleanField(default=False)
	is_surgical_approach_form = models.BooleanField(default=False)
	is_deworming_form = models.BooleanField(default=False)
	is_vaccination_form = models.BooleanField(default=False)
	is_artificial_insemination_form = models.BooleanField(default=False)
	is_calf_registration_form = models.BooleanField(default=False)
	is_livestock_inventory_form = models.BooleanField(default=False)
	is_farm_consultation_form = models.BooleanField(default=False)
	is_pregnancy_diagnosis_form = models.BooleanField(default=False)
	farm_name = models.ForeignKey(Farm, on_delete=models.CASCADE)
	species_affected = models.IntegerField(choices=SPECIES_CHOICES, default=0)
	num_of_species_affected = models.IntegerField()
	report_created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-report_created_on']

class Sick_Approach_Form(models.Model):
	form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	disease_nature = models.IntegerField(choices=DISEASE_CHOICES, default=0)
	clinical_sign = models.CharField(max_length=100, default='')
	disease_diagnosis = models.IntegerField(choices=DIAGNOSIS_CHOICES, default=0)
	differential_diagnosis = models.CharField(max_length=100, default='')
	final_diagnosis = models.CharField(max_length=100, default='')
	sickness_duration = models.DurationField()
	sickness_history = models.CharField(max_length=100, default='')
	drug_choices = models.CharField(max_length=100, default='')
	treatment_duration = models.DurationField()
	start_dose_date = models.DateTimeField()
	prognosis = models.IntegerField(choices=PROGNOSIS_CHOICES, default=0)
	harmony_with_clinic_signs_and_lab = models.IntegerField(choices=YES_NO_CHOICES, default=0)
	cause_of_death_if_in_no_harmony = models.CharField(max_length=100, null=True, blank=True)
	disease_one_of_the_zoonotic = models.IntegerField(choices=YES_NO_CHOICES, default=0)
	advice_given_if_zoonotic = models.CharField(max_length=100, null=True, blank=True)
	relapse = models.IntegerField(choices=YES_NO_CHOICES, default=0)
	cause_if_relapse = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Sick Approach Form'
	
 	
