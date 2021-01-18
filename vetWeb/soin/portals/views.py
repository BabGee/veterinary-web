from django.shortcuts import render
from user.models import Vet_Officer


def portal_vet(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexvet.html', context)


def portal_farmer(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexfarmer.html', context)



def portal_student(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexstudent.html', context)  



def clinical_approach(request):
    return render(request, 'portals/clinical_approach.html') 


def sick_approach(request):
    # if request.method == "POST":
    #     form = forms.SickApproachForm(request.POST)

    #     if form.is_valid():
    #         form.is_sick_approach_form = True
    #         form.farm_name = form.cleaned_data.get('farm_name')
    #         form.species_affected = form.cleaned_data.get('species_affected')            
    #         form.num_of_species_affected = form.cleaned_data.get('num_of_species_affected')
    #         form.form = Sick_Approach_Form.objects.create(form=form)
    #         form.disease_nature = form.cleaned_data.get('nature_of_disease')
    #         form.clinical_sign = form.cleaned_data.get('clinical_sign')
    #         form.disease_diagnosis = form.cleaned_data.get('disease_diagnosis')
    #         form.differential_diagnosis = form.cleaned_data.get('differential_diagnosis')
    #         form.final_diagnosis = form.cleaned_data.get('final_diagnosis')
    #         form.sickness_duration = form.cleaned_data.get('sickness_duration')
    #         form.sickness_history = form.cleaned_data.get('sickness_history')
    #         form.drug_choices = form.cleaned_data.get('drug_choice')
    #         form.treatment_duration = form.cleaned_data.get('treatment_duration')
    #         form.start_dose_date = form.cleaned_data.get('start_dose_date')
    #         form.prognosis = form.cleaned_data.get('prognosis')
    #         form.harmony_with_clinic_signs_and_lab = form.cleaned_data.get('pathological_conditions_in_harmony_with_the_clinic_signs_and_lab_reports')
    #         form.cause_of_death_if_in_no_harmony = form.cleaned_data.get('cause_of_the_death_if_no')
    #         form.disease_one_of_the_zoonotic = form.cleaned_data.get('disease_zoonotic')
    #         form.advice_given_if_zoonotic = form.cleaned_data.get('advice_given_if_zoonotic')
    #         form.relapse = form.cleaned_data.get('relapse')
    #         form.cause_if_relapse = form.cleaned_data.get('cause_if_relapse')
    #         form.save()
            

    #     # if form.is_valid():
    #     #     form.save()
    #     #     farm_name = form.cleaned_data.get('username')
    #     #     messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #     #     return redirect('clinical-approach')

    # else:
    #     form = forms.SickApproachForm()

    # context = {
    #     'sick_approach_form':form
    #     }
    return render(request, 'portals/sick_approach.html') 







# class SickApproachFormView(CreateView):
# 	def get_success_url(form):
# 		return reverse('vet-portal')
        
# 	model = Sick_Approach_Form
# 	template_name = 'portals/sick_approach.html'
# 	form_class = forms.SickApproachForm
	
# 	def get_context_data(form, **kwargs):
# 		context = super(SickApproachFormView, form).get_context_data(**kwargs)
# 		context['sick_approach_form'] = form.form_class
# 		return context

def dead_approach(request):
    # if request.method == "POST":
    #     form = forms.DeadApproachForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('farm_name')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('clinical-approach')

    # else:
    #     form = forms.DeadApproachForm()

    # context = {
    #     'dead_approach_form':form
    # }
    return render(request, 'portals/dead_approach.html', context)  

def surgical_approach(request):
    # if request.method == "POST":
    #     form = forms.SurgicalApproachForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('farm_name')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('clinical-approach')

    # else:
    #     form = forms.SurgicalApproachForm()

    # context = {
    #     'surgical_approach_form':form
    # }
    return render(request, 'portals/surgical_approach.html')  


def deworming(request):
    # if request.method == "POST":
    #     form = forms.DewormingForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {deworming} Succesfully Saved')
    #         return redirect('deworming')

    # else:
    #     form = forms.DewormingForm()

    # context = {
    #     'deworming_form':form
    # }
    return render(request, 'portals/deworming.html') 

    
def vaccination(request):
    # if request.method == "POST":
    #     form = forms.vaccination_form(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {vaccination} Succesfully Saved')
    #         return redirect('vaccination')

    # else:
    #     form = forms.vaccination_form()

    # context = {
    #     'vaccination_form':form
    # }
    return render(request, 'portals/vaccination.html')


def breeding_record(request):
    return render(request, 'portals/breeding_record.html')

def artificial_insemination(request):
    # if request.method == "POST":
    #     form = forms.ArtificialInseminationForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('artificial-insemination')

    # else:
    #     form = forms.ArtificialInseminationForm()

    # context = {
    #     'artificial_insemination_form':form
    # }
    return render(request, 'portals/artificial_insemination.html') 


def calf_registration(request):
    # if request.method == "POST":
    #     form = forms.CalfRegistrationForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('calf-registration')

    # else:
    #     form = forms.CalfRegistrationForm()

    # context = {
    #     'calf_registration_form':form
    # }
    return render(request, 'portals/calf_registration.html')


def livestock_inventory(request):
    # if request.method == "POST":
    #     form = forms.LivestockInventoryForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('livestock-inventory')

    # else:
    #     form = forms.LivestockInventoryForm()

    # context = {
    #     'livestock_inventory_form':form
    # }
    return render(request, 'portals/livestock_inventory.html')


def pregnancy_diagnosis(request):
    # if request.method == "POST":
    #     form = forms.PregnancyDiagnosisForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {farm_name} Succesfully Saved')
    #         return redirect('pregnancy_diagnosis')

    # else:
    #     form = forms.PregnancyDiagnosisForm()

    # context = {
    #     'pregnancy_diagnosis_form':form
    # }
    return render(request, 'portals/pregnancy_diagnosis.html')
    

def consultation(request):
    # if request.method == "POST":
    #     form = forms.FarmConsultationForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         farm_name = form.cleaned_data.get('username')
    #         messages.success(request,f'Details for {consultation} Succesfully Saved')
    #         return redirect('consultation')

    # else:
    #     form = forms.FarmConsultationForm()

    # context = {
    #     'consultation_form':form
    # }
    return render(request, 'portals/consultation.html')




     