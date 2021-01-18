from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='user_pics')

    def __str__(self):
        return self.user.username     

def post_save_profile_create(sender, instance, created,*args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)                                       
        
post_save.connect(post_save_profile_create, sender=User)            
