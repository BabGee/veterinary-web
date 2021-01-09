"""soin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views
from portals import views as portal_views

urlpatterns = [
    path('', include('vet.urls')),
    path('admin/', admin.site.urls),
    #users sign up
    path('user/signup/vet_officer/', user_views.VetOfficerSignUpView.as_view(), name='vet-register'),
    path('user/signup/farmer/',user_views.FarmerSignUpView.as_view(),name='farmer_register'),
    path('user/signup/student/',user_views.StudentSignUpView.as_view(),name='student_register'),
    #users login 
    path('user/login/',user_views.user_login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    #users portals
    path('vet_portal/', portal_views.portal_vet, name='vet-portal'),
    path('farmer_portal/', portal_views.portal_farmer, name='farmer-portal'),
    path('student_portal/', portal_views.portal_student, name='student-portal'),
    #vet forms
    path('clinical_approach/',user_views.clinical_approach,name='clinical-approach'),
    #path('sick_approach', user_views.SickApproachFormView.as_view(), name='sick-approach'),
    path('sick_approach', user_views.sick_approach, name='sick-approach'),
    path('dead_approach', user_views.dead_approach, name='dead-approach'),
    path('surgical_approach',user_views.surgical_approach, name='surgical-approach'),
    path('deworming',user_views.deworming,name='deworming'),
    path('vaccination',user_views.vaccination,name='vaccination'),
    path('breeding_record/',user_views.breeding_record,name='breeding_record'),
    path('artificial_insemination', user_views.artificial_insemination, name='artificial-insemination'),
    path('pregnancy_diagnosis',user_views.pregnancy_diagnosis,name='pregnancy_diagnosis'),
    path('calf_registration', user_views.calf_registration, name='calf-registration'),
    path('livestock_inventory', user_views.livestock_inventory, name='livestock-inventory'),
    path('consultation',user_views.consultation,name='consultation')
]
