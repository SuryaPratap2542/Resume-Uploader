from django.contrib import admin

# Register your models here.
from .models import Resume

@admin.register(Resume)
class ResumeModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city','profile_image','my_file']
