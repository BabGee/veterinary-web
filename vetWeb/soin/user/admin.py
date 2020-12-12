from django.contrib import admin
from .models import Vet_Officer, Farmer, Student, User

admin.site.register(User)
admin.site.register(Vet_Officer)
admin.site.register(Farmer)
admin.site.register(Student)