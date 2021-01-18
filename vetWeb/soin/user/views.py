from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse

from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
#from django.views.generic import View

from django.contrib.auth import get_user_model

from django.contrib.auth import login, authenticate
from .models import User
from django.contrib.auth.forms import AuthenticationForm   



User = get_user_model()

class VetOfficerSignUpView(CreateView):
	def get_success_url(form):
		return reverse('login')
    
	model = User
	form_class = forms.VetOfficerSignUpForm
	template_name = 'user/register.html'

	def get_context_data(form, **kwargs):
		context = super(VetOfficerSignUpView, form).get_context_data(**kwargs)
		context['form'] = form.form_class
		return context
    

class FarmerSignUpView(CreateView):
	def get_success_url(form):
		return reverse('login')
	model = User
	form_class = forms.FarmerSignUpForm
	template_name = 'user/register.html'

	def get_context_data(form, **kwargs):
		context = super(FarmerSignUpView, form).get_context_data(**kwargs)
		context['form'] = form.form_class
		return context


class StudentSignUpView(CreateView):
	def get_success_url(form):
		return reverse('login')
        
	model = User
	template_name = 'user/register.html'
	form_class = forms.StudentSignUpForm
	
	def get_context_data(form, **kwargs):
		context = super(StudentSignUpView, form).get_context_data(**kwargs)
		context['form'] = form.form_class
		return context
		

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.is_vet_officer:
               return redirect('vet-portal')
            elif user.is_authenticated and user.is_farmer:
                return redirect('farmer-portal')
            elif user.is_authenticated and user.is_student:
                return redirect('student-portal')    
        else:
            messages.error(request, 'invalid Credentials')
    
    return render(request, 'user/login.html', {'form':form})

