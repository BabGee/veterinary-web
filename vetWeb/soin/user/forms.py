from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Vet_Officer, Farmer, Student, Farm

User = get_user_model()

class VetOfficerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
		
	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'form-control'
			}
		)
	)
	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,12}$')
	kvb_number = forms.IntegerField()
	
	password1 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)
	
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','first_name','last_name','kvb_number','phone_number','email','password1', 'password2',)
		
	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_vet_officer = True
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.phone_number = self.cleaned_data.get('phone_number')
		user.save()
		vet_officer = Vet_Officer.objects.create(user=user)
		vet_officer.kvb_number = self.cleaned_data.get('kvb_number')
		vet_officer.save()
		return user
	
class FarmerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
	email = forms.EmailField()
	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,12}$')
	farm_name  = forms.CharField(max_length=20)
	location = forms.CharField(max_length=30)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','farm_name','email', 'location','password1', 'password2']
			
	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_farmer = True
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.phone_number = self.cleaned_data.get('phone_number')
		user.save()
		farmer = Farmer.objects.create(user=user)
		farmer.farm_name = self.cleaned_data.get('farm_name')
		farmer.location = self.cleaned_data.get('location')
		farmer.save()
		return user

class StudentSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=10,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
	email = forms.EmailField()
	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,12}$')
	student_number = forms.CharField(max_length=20)
	college_name = forms.CharField(max_length=20)
	location = forms.CharField(max_length=30)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','student_number','college_name', 'phone_number', 'email', 'location','password1', 'password2']	

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.phone_number = self.cleaned_data.get('phone_number')
		user.save()
		student = Student.objects.create(user=user)
		student.student_number = self.cleaned_data.get('student_number')
		student.college_name = self.cleaned_data.get('college_name')
		student.location = self.cleaned_data.get('location')
		student.save()
		return user
