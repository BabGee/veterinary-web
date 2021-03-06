from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from portals.models import Vet_Forms, Sick_Approach_Form, Death_Approach_Form, Surgical_Approach_Form, Deworming_Form, Vaccination_Form, Artificial_Insemination_Form, Calf_Registration_Form, Livestock_Inventory_Form, Pregnancy_Diagnosis_Form

User = get_user_model()


class SickApproachForm(ModelForm):
	class Meta:
		model = Sick_Approach_Form
		exclude = ['vet_form', 'report_created_on',]


class DeathApproachForm(ModelForm):
	class Meta:
		model = Death_Approach_Form
		exclude = ['vet_form', 'report_created_on',]


class SurgicalApproachForm(ModelForm):
	class Meta:
		model = Surgical_Approach_Form
		exclude = ['vet_form', 'report_created_on',]


class DewormingForm(ModelForm):
	class Meta:
		model = Deworming_Form
		exclude = ['vet_form', 'report_created_on',]


class VaccinationForm(ModelForm):
	class Meta:
		model = Vaccination_Form
		exclude = ['vet_form', 'report_created_on',]


class ArtificialInseminationForm(ModelForm):
	class Meta:
		model = Artificial_Insemination_Form
		exclude = ['vet_form', 'report_created_on',]


class CalfRegistrationForm(ModelForm):
	class Meta:
		model = Calf_Registration_Form
		exclude = ['vet_form', 'report_created_on',]


class LivestockInventoryForm(ModelForm):
	class Meta:
		model = Livestock_Inventory_Form
		exclude = ['vet_form', 'report_created_on',]


class PregnancyDiagnosisForm(ModelForm):
	class Meta:
		model = Pregnancy_Diagnosis_Form
		exclude = ['vet_form', 'report_created_on',]		














# SPECIES_CHOICES = (
#     ('0', 'cattle'),
#     ('1', 'sheep'),
# 	('2', 'goat'),
# 	('3', 'donkey'),
# 	('4', 'dog'),
# 	('5', 'horse'),
# 	('6', 'poulry'),
# 	('7','others')
# )

# SPECIES_TARGETTED = (
# 	('C', 'cattle'),
#     ('S', 'sheep'),
# 	('g', 'goat'),
# 	('dk', 'donkey'),
# 	('d', 'dog'),
# 	('h', 'horse'),
# 	('p', 'poulry'),
# 	('O','others')
# )

# SEX_CHOICES = (
# 	('M','male'),
# 	('F','female')
# )

# DISEASE_CHOICES = (
# 	('A','acute'),
# 	('S','sub_acute')

# )
# DIAGNOSIS_CHOICES = (
# 	('C','clinical_signs'),
# 	('L','laboratory')
# )
# PROGNOSIS_CHOICES=(
# 	('G','good'),
# 	('F','fair'),
# 	('P','poor')
# )

# VACCINATION_CHOICES=(
# 	('M','Mass_vaccination'),
# 	('R','Ring_vaccination'),
# 	('I','Individual')
# )
# OPERATION_CHOICES=(
# 	('C','c_section'),
# 	('I','interstinal_torsion'),
# 	('T','tumor_extraction'),
# 	('C','canine_spaying'),
# 	('H','hernia'),
# 	('W','Warts_etraction'),
# 	('C','castration'),
# 	('S','skin_injuries'),
# 	('F','fructure'),
# 	('R','rumenatomy'),
# 	('O','other')

# )
# NATURE_CHOICES=(
# 	('A','Alive'),
# 	('D','Dead')
# )

# MANAGE_CHOICES=(
# 	('Y','Yes'),
# 	('N','No')
# )

# STATUS_CHOICES=(
# 	('H','Healthy'),
# 	('D','Deformed')
# )

# RESULT_CHOICES=(
# 	('P','positive'),
# 	('N','Negative')
# )

# PICK_CHOICES=(
# 	('Y','Yes'),
# 	('N','No')
# )
# INSURED_CHOICES=(
# 	('Y','Yes'),
# 	('N','No')
# )
# BREECHING_LEVEL=(
# 	('F','First'),
# 	('S','Second'),
# 	('T','Third'),
# 	('P','Pedegree')
# )
# PICK_REPORT=(
# 	('E','Early'),
# 	('L','Late')
# )


# class SurgicalApproachForm(forms.Form):
# 	farm_name = forms.CharField(required=True)
# 	species_affected = forms.ChoiceField(widget=forms.RadioSelect, choices=SPECIES_CHOICES)	
# 	sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)	
# 	age = forms.IntegerField(required=False)
# 	num_animals = forms.IntegerField(required=True)
# 	identification_number_of_the_animal = forms.IntegerField(required=True)
# 	nature_of_the_operation = forms.ChoiceField(widget=forms.RadioSelect, choices=OPERATION_CHOICES)
# 	if_other_specify = forms.CharField(required=False)
# 	date_of_operation = forms.CharField(required=False)
# 	post_operation_management = forms.CharField(required=True)
# 	prognosis = forms.CharField(required=True)
# 	name_of_the_farm = forms.CharField(required=True)
# 	name_of_the_owner = forms.CharField(required=True)
# 	mobile_number = forms.IntegerField(required=True)
# 	location = forms.CharField(required=True)
# 	name_of_the_veterinary_officer = forms.CharField(required=False)
# 	comment = forms.CharField(required=False)
	
# class DewormingForm(forms.Form):
# 	species_targetted = forms.ChoiceField(widget=forms.RadioSelect,choices=SPECIES_CHOICES)
# 	If_other_specify = forms.CharField(required=False)
# 	Number_of_adults = forms.IntegerField(required=True)
# 	Number_of_young_ones = forms.CharField(required=True)
# 	Name_of_the_animal = forms.CharField(required=True)
# 	Registration_number = forms.IntegerField(required=True)
# 	Body_condition_of_the_animal = forms.CharField(required=False)
# 	Date_of_deworming = forms.IntegerField(required=True)
# 	Drug_of_choice = forms.CharField(required=False)
# 	Target_parasites = forms.CharField(required=False)
# 	Withdrawal_period = forms.IntegerField(required=False)
# 	Any_side_effect = forms.CharField(required=False)
# 	Next_date_deworming = forms.IntegerField(required=True)
# 	Name_of_the_farmer = forms.CharField(required=True)
# 	Mobile_number = forms.IntegerField(required=True)
# 	Name_of_the_veterinary_officer = forms.CharField(required=True)
# 	Mobile_number = forms.IntegerField(required=True)
# 	comment = forms.CharField(required=False)
	
# class vaccination_form(forms.Form):
# 	species_targetted = forms.ChoiceField(widget=forms.RadioSelect, choices=SPECIES_CHOICES)
# 	If_other_specify = forms.CharField(required=False)
# 	Number_of_animals_vaccinated = forms.IntegerField(required=True)
# 	Age_of_the_animal = forms.IntegerField(required=True)
# 	sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
# 	breed_of_the_animal = forms.CharField(required=False)
# 	colour_of_the_animal = forms.CharField(required=False)
# 	other_description = forms.CharField(required=False)
# 	The_disease_target = forms.CharField(required=True)
# 	Vaccines_used = forms.CharField(required=False)
# 	Batch_number = forms.IntegerField(required=False)
# 	Date_of_vaccination = forms.IntegerField(required=True)
# 	Next_date_of_vaccination = forms.IntegerField(required=True)
# 	Name_of_the_crush = forms.CharField(required=False)
# 	Nature_of_the_vacination_program = forms.ChoiceField(widget=forms.RadioSelect,choices=VACCINATION_CHOICES)
# 	Name_of_the_owner = forms.CharField(required=True)
# 	mobile_number = forms.IntegerField(required=True)
# 	location = forms.CharField(required=True)
# 	name_of_the_veterinary_officer = forms.CharField(required=True)
# 	registration_number_of_the_veterinary_officer = forms.IntegerField(required=True)
# 	comments = forms.CharField(required=False)

# class ArtificialInseminationForm(forms.Form):
# 	Name_of_the_cow =  forms.CharField(required=False)
# 	Age_of_the_animal = forms.IntegerField(required=False)
# 	identification_number = forms.IntegerField(required=False)
# 	Time_of_heat_sign = forms.CharField(required=False)
# 	Time_of_insemination = forms.IntegerField(required=True)
# 	Date_of_insemination = forms.IntegerField(required=True)
# 	Nature_of_the_breeding = forms.CharField(required=False)
# 	Sire_name = forms.CharField(required=True)
# 	Bull_code = forms.CharField(required=False)
# 	Sire_origin = forms.CharField(required=True)
# 	sex_of_the_calf_born = forms.CharField(required=True)
# 	Date_of_birth = forms.IntegerField(required=True)
# 	Nature_of_birth = forms.ChoiceField(widget=forms.RadioSelect, choices=NATURE_CHOICES)
# 	Number_of_repeat = forms.IntegerField(required=False)
# 	Abortion_rate = forms.CharField(required=False)
# 	Reason_for_the_cause_of_abortion = forms.CharField(required=False)
# 	Breed_used =forms.CharField(required=False)
# 	Name_of_the_bull = forms.CharField(required=False)
# 	Code_number = forms.IntegerField(required=False)
# 	Source_of_the_semen = forms.CharField(required=False)
# 	Date_of_repeat_checked = forms.IntegerField(required=True)
# 	Date_of_pregnancy_diagnosis = forms.CharField(required=True)
# 	Expected_date_of_calving = forms.IntegerField(required=True)
# 	Farmer_name = forms.CharField(required=True)
# 	Farmer_location = forms.CharField(required=True)
# 	mobile_number = forms.IntegerField(required=True)
# 	Name_of_the_inseminator = forms.CharField(required=True)
# 	Registration_number = forms.IntegerField(required=True)

# class CalfRegistrationForm(forms.Form):
# 	Date_of_birth = forms.IntegerField(required=True)
# 	Sex_of_the_calf = forms.CharField(required=True)
# 	Birth_weight = forms.IntegerField(required=True)
# 	Breed_of_the_calf = forms.CharField(required=True)
# 	Colour_of_the_breed = forms.CharField(required=True)
# 	Name_of_the_calf = forms.CharField(required=True)
# 	Registration_number = forms.IntegerField(required=True)
# 	Status_of_the_calf = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES)
# 	Breeching_level_of_the_calf = forms.ChoiceField(widget=forms.RadioSelect, choices=BREECHING_LEVEL)
# 	Give_the_sire_details = forms.CharField(required=False)
# 	Expected_date_of_weaning = forms.CharField(required=False)

# class LivestockInventoryForm(forms.Form):
# 	species_targetted = forms.ChoiceField(widget=forms.RadioSelect, choices=SPECIES_CHOICES)
# 	Number_of_the_female_animals = forms.IntegerField(required=True)
# 	Number_of_the_male_animals = forms.IntegerField(required=True)
# 	Name_of_the_animal = forms.CharField(required=True)
# 	Registration_number_of_the_animal = forms.IntegerField(required=True)
# 	Number_of_live_animals = forms.IntegerField(required=True)
# 	Number_of_dead_animals = forms.IntegerField(required=True)
# 	Specify_the_cause_of_the_dead = forms.CharField(required=True)
# 	Is_your_animals_insured = forms.ChoiceField(widget=forms.RadioSelect, choices=INSURED_CHOICES)
# 	If_yes_give_insuring_company = forms.CharField(required=True)
# 	Date_of_culling = forms.IntegerField(required=True)
# 	Give_reason_for_culling = forms.CharField(required=True)
# 	Attach_photos_of_your_animal = forms.CharField(required=True)
# 	Who_normally_treat_your_animals = forms.CharField(required=True)
# 	Give_the_name_of_the_veterinary_offier_in_charge_of_your_livestock = forms.CharField(required=True)

# class FarmConsultationForm(forms.Form):
# 	Name_of_the_farm = forms.CharField(required=True)
# 	Name_of_the_owner = forms.CharField(required=True)
# 	Mobile_number = forms.IntegerField(required=True)
# 	County = forms.CharField(required=True)
# 	Sub_County = forms.CharField(required=True)
# 	Location = forms.CharField(required=True)
# 	Dairy_cows_unit = forms.CharField(required=True)
# 	Beef_production_unit = forms.CharField(required=True)
# 	Poultry_production_unit = forms.CharField(required=True)
# 	Sheep_production_unit = forms.CharField(required=True)
# 	Goat_production = forms.CharField(required=True)
# 	Canine_keeping = forms.CharField(required=True)
# 	Other_livestock = forms.CharField(required=True)
# 	Give_recommendation = forms.CharField(required=True)
# 	Grazing_system_and_pasture_managemnt = forms.CharField(required=True)
# 	Disease_control = forms.CharField(required=True)
# 	Parasite_control = forms.CharField(required=True)
# 	Farm_Biosecurity = forms.CharField(required=True)
# 	Culling_and_selecion = forms.CharField(required=True)
# 	Farm_records = forms.CharField(required=True)
# 	Livestock_housing = forms.CharField(required=True)
# 	Is_the_farm_managed_by_a_veterinary_officer_or_a_livestock_officer = forms.ChoiceField(widget=forms.RadioSelect, choices=MANAGE_CHOICES)
# 	If_no_who_is_the_farm_consultant = forms.CharField(required=True)
# 	Name_of_the_veterinary_officer_in_charge = forms.CharField(required=True)
# 	Registration_number = forms.IntegerField(required=True)
# 	Comments = forms.CharField(required=True)

# class PregnancyDiagnosisForm(forms.Form):
# 	Name_of_the_cow = forms.CharField(required=True)
# 	Identification_number = forms.IntegerField(required=True)
# 	Date_of_insemination = forms.IntegerField(required=True)
# 	Date_of_pregnancy_diagnosis = forms.IntegerField(required=True)
# 	The_result_of_diagnosis = forms.ChoiceField(widget=forms.RadioSelect, choices=RESULT_CHOICES)
# 	If_the_result_is_positve_give_the_approximate_age_of_the_fetus = forms.IntegerField(required=True)
# 	If_the_result_is_negative_give_your_observation = forms.CharField(required=True)
# 	Next_date_of_pregnancy_diagnosis = forms.IntegerField(required=True)
# 	Expected_date_of_delivery = forms.IntegerField(required=True)
# 	Name_of_the_owner = forms.CharField(required=True)
# 	Location = forms.CharField(required=True)
# 	Mobile_number = forms.IntegerField(required=True)
# 	Name_of_the_veterinary_officer = forms.CharField(required=True)
# 	Mobile_number = forms.IntegerField(required=True)
# 	Comment = forms.CharField(required=True)



