from django.db import models
from django.utils import timezone
# Create your models here.
# Name
# USN
# DOB
# Gender
# Region
# Highest edu
# Disability 
# Starting month
# Date of registration
# Start date
# Sem
# College
# Username
# Password
# Mail
# phone
# Sub Code (Code module)
# Number of previous attempts
# Imd band
# Age band
# Credits
# Sum click

class user(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    usn = models.CharField(max_length=100, null=False, unique=True)
    dob = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=100)
    # highest_edu = models.CharField(max_length=100)
    disability = models.CharField(max_length=100)
    sem = models.IntegerField()
    college = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 )
    phone = models.BigIntegerField()
    enroll_date = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.name
# class parameters(models.Model):
#     user = models.ForeignKey(user, on_delete=models.CASCADE)
#     sub_code = models.CharField(max_length=10)
#     prev_attempts = models.IntegerField()
#     imd_band = models.CharField(max_length=10)
#     age_band = models.CharField(max_length=10)
#     credits = models.IntegerField()
#     sum_click = models.IntegerField()

        
class feedback(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


