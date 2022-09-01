from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=20)
    company_code = models.CharField(max_length=20)
    strength = models.IntegerField()
    website = models.CharField(max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)
