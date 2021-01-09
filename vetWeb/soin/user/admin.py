from django.contrib import admin
from .models import Vet_Officer, Farmer, Farm, Student, User, Vet_Forms, Sick_Approach_Form

admin.site.register(User)
admin.site.register(Vet_Officer)
admin.site.register(Farmer)
admin.site.register(Student)
admin.site.register(Vet_Forms)
admin.site.register(Sick_Approach_Form)
admin.site.register(Farm)