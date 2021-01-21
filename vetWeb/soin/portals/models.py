from django.db import models
from user.models import Farm

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


OPERATION_CHOICES=(
	('C','c_section'),
 	('I','interstinal_torsion'),
 	('T','tumor_extraction'),
 	('C','canine_spaying'),
 	('H','hernia'),
 	('W','Warts_etraction'),
 	('C','castration'),
 	('S','skin_injuries'),
 	('F','fructure'),
	('R','rumenatomy'),
 	('O','other'),
)

VACCINATION_CHOICES=(
	('M','Mass_vaccination'),
 	('R','Ring_vaccination'),
 	('I','Individual')
)

SEX_CHOICES = (
 	('M','male'),
 	('F','female')
 )


NATURE_CHOICES=(
 	('A','Alive'),
 	('D','Dead')
 )



STATUS_CHOICES=(
 	('H','Healthy'),
 	('D','Deformed')
 )

BREECHING_LEVEL=(
 	('F','First'),
 	('S','Second'),
 	('T','Third'),
 	('P','Pedegree')
)

RESULT_CHOICES=(
 	('P','positive'),
 	('N','Negative')
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
	report_created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-report_created_on']


class Sick_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_affected = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	num_of_species_affected = models.IntegerField(default=1)
	disease_nature = models.CharField(max_length=20, choices=DISEASE_CHOICES, default='0')
	clinical_sign = models.CharField(max_length=100, default='')
	disease_diagnosis = models.CharField(max_length=20, choices=DIAGNOSIS_CHOICES, default='0')
	differential_diagnosis = models.CharField(max_length=100, default='')
	final_diagnosis = models.CharField(max_length=100, default='')
	sickness_duration = models.DurationField()
	sickness_history = models.CharField(max_length=100, default='')
	drug_choices = models.CharField(max_length=100, default='')
	treatment_duration = models.DurationField()
	start_dose_date = models.DateTimeField()
	prognosis = models.CharField(max_length=20, choices=PROGNOSIS_CHOICES, default='G')
	harmony_with_clinic_signs_and_lab = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	cause_of_death_if_in_no_harmony = models.CharField(max_length=100, null=True, blank=True)
	disease_one_of_the_zoonotic = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	advice_given_if_zoonotic = models.CharField(max_length=100, null=True, blank=True)
	relapse = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	cause_if_relapse = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Sick Approach Form'
	

class Death_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_dead = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	num_of_species_dead = models.IntegerField(default=1)
	case_history = models.CharField(max_length=100, default='')
	mortality_rate = models.CharField(max_length=100, default='')
	death_time = models.DateTimeField()
	signs_of_cadever_on_the_ground = models.CharField(max_length=200)
	carcass_opened_for_the_pm = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	if_yes_pathological_signs = models.CharField(max_length=100, null=True, blank=True)
	if_no_reason = models.CharField(max_length=100, null=True, blank=True)
	sample_sent_lab = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	if_yes_lab_report = models.CharField(max_length=100, null=True, blank=True)
	death_cause_notifiable = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0')
	if_yes_message_to_relevant_body = models.CharField(max_length=100, null=True, blank=True)
	intervention_regards_to_death = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Death Approach Form'


class Surgical_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_operated_on = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	num_of_animals_operated_on = models.IntegerField(default=1)
	operation_nature= models.CharField(max_length=20, choices=OPERATION_CHOICES, default='0')
	if_other_specify = models.CharField(max_length=100, null=True, blank=True)
	operation_date = models.DateTimeField()
	post_operation_management = models.CharField(max_length=100, default='')
	prognosis = models.CharField(max_length=100, default='')
	comment = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Surgical Approach Form'


class Deworming_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	number_of_adults = models.IntegerField(default=1)
	number_of_young_ones = models.IntegerField(default=1)
	body_condition_of_the_animal = models.CharField(max_length=20, choices=PROGNOSIS_CHOICES, default='G')
	date_of_deworming = models.DateTimeField()
	drug_choices = models.CharField(max_length=100, default='')
	target_parasites = models.CharField(max_length=100, null=True, blank=True)
	withdrawal_period = models.DurationField()
	side_effects = models.CharField(max_length=100, null=True, blank=True)
	next_date_deworming = models.DateTimeField()
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Deworming Approach Form'


class Vaccination_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	number_of_animals_vaccinated= models.IntegerField(default=1)
	animal_breed = models.CharField(max_length=100, null=True, blank=True)
	other_description = models.CharField(max_length=100, null=True, blank=True)
	targetted_disease = models.CharField(max_length=20)
	vaccines_used = models.CharField(max_length=100, null=True, blank=True)
	date_of_vaccination = models.DateTimeField()
	next_date_of_vaccination = models.DateTimeField()
	name_of_the_crush = models.CharField(max_length=100, null=True, blank=True)
	nature_of_the_vacination_program = models.CharField(max_length=200, choices=VACCINATION_CHOICES, default='M')
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Vaccination Approach Form'


class Artificial_Insemination_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	cow_code = models.CharField(max_length=20, unique=True)
	age_of_animal = models.IntegerField(default=1)
	time_of_heat_sign = models.DateTimeField()
	date_of_insemination = models.DateTimeField()
	nature_of_the_breeding = models.CharField(max_length=100, null=True, blank=True)
	sire_name = models.CharField(max_length=200)
	sire_origin = models.CharField(max_length=200)
	bull_code= models.CharField(max_length=100, null=True, blank=True)
	sex_of_the_calf_born = models.CharField(max_length=20, choices=SEX_CHOICES, default='M')
	date_of_birth = models.DateTimeField()
	nature_of_birth = models.CharField(max_length=20, choices=NATURE_CHOICES, default='A')
	number_of_repeat = models.CharField(max_length=100, null=True, blank=True)
	abortion_rate = models.CharField(max_length=100, null=True, blank=True)
	reason_for_the_cause_of_abortion = models.CharField(max_length=100, null=True, blank=True)
	breed_used = models.CharField(max_length=100, null=True, blank=True)
	source_of_semen = models.CharField(max_length=100, null=True, blank=True)
	date_of_repeat_checked = models.DateTimeField()
	date_of_pregnancy_diagnosis = models.DateTimeField()
	expected_date_of_calving = models.DateTimeField()
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Artificial Approach Form'


class Calf_Registration_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	calf_code = models.CharField(max_length=20)
	sex_of_the_calf = models.CharField(max_length=20, choices=SEX_CHOICES, default='M')
	birth_weight = models.IntegerField()
	breed_of_the_calf = models.CharField(max_length=20)
	colour_of_the_breed= models.CharField(max_length=20)
	status_of_the_calf = models.CharField(max_length=100, choices=STATUS_CHOICES, default='H')
	breeching_level_of_the_calf = models.CharField(max_length=100, choices=BREECHING_LEVEL, default='F')
	sire_details = models.CharField(max_length=100, null=True, blank=True)
	expected_date_of_weaning = models.DateTimeField()
	
	def __str__(self):
		return f'Name of form: Calf Registration Approach Form'


class Livestock_Inventory_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0')
	number_of_the_male_animals= models.IntegerField(default=1)
	number_of_the_female_animals= models.IntegerField(default=1)
	number_of_live_animals= models.IntegerField(default=1)
	number_of_dead_animals= models.IntegerField(default=1)
	specify_the_cause_of_the_dead = models.CharField(max_length=100, null=True, blank=True)
	is_your_animals_insured = models.CharField(max_length=20, choices=YES_NO_CHOICES, default='Y')
	if_yes_give_insuring_company = models.CharField(max_length=100, null=True, blank=True)
	date_of_culling = models.DateTimeField()
	give_reason_for_culling = models.CharField(max_length=200)

	def __str__(self):
		return f'Name of form: Livestock Inventory Approach Form'


class Pregnancy_Diagnosis_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	cow_code = models.CharField(max_length=20)
	date_of_insemination = models.DateTimeField()
	date_of_pregnancy_diagnosis = models.DateTimeField()
	result_of_diagnosis = models.CharField(max_length=200, choices=RESULT_CHOICES, default='P')
	if_result_is_negative_give_observation = models.CharField(max_length=100, null=True, blank=True)
	next_date_of_pregnancy_diagnosis = models.DateTimeField()
	expected_date_of_delivery = models.DateTimeField()
	comment = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Pregnancy Diagnosis Form'








