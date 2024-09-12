from django.contrib import admin
from .models import Alumni, Donation, SuccessStory

# Register the Alumni model
@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'graduation_year', 'field_of_study', 'skills', 'area_of_interest')
    search_fields = ('name', 'email', 'field_of_study', 'skills', 'area_of_interest')

# Register the Donation model
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'message')
    search_fields = ('name', 'email')

# Register the SuccessStory model
@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'alumni')
    search_fields = ('title', 'description', 'alumni__name')

