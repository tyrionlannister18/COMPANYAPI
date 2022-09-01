from django.contrib import admin
from .models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','email_id','company_code','strength','website','created_time']

admin.site.register(Company,CompanyAdmin)