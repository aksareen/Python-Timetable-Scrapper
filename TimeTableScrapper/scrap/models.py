from django.db import models

class students(models.Model):
    regno = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    
