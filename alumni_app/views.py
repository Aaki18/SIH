from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Alumni, Donation, SuccessStory, Mentorship
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json

# Form for donation
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'message']

# Form for mentorship
class MentorshipForm(forms.ModelForm):
    class Meta:
        model = Mentorship
        fields = ['skills', 'area_of_interest']

def alumni_list(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni_list.html', {'alumni': alumni})

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
        else:
            return render(request, 'donate.html', {'form': form, 'error': 'Invalid data'})
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def success_stories(request):
    stories = SuccessStory.objects.all()
    return render(request, 'success_stories.html', {'stories': stories})

@csrf_exempt
def offer_mentorship(request):
    if request.method == 'POST':
        form = MentorshipForm(request.POST)
        if form.is_valid():
            mentorship = form.save(commit=False)
            # Assume you have a way to get the current user’s alumni instance
            alumni_instance = Alumni.objects.get(email=request.POST['alumni_email'])
            mentorship.alumni = alumni_instance
            mentorship.save()
            return redirect('view_recommendation')
        else:
            return render(request, 'offer_mentorship.html', {'form': form, 'error': 'Invalid data'})
    else:
        form = MentorshipForm()
    return render(request, 'offer_mentorship.html', {'form': form})

def view_recommendation(request):
    # Example of retrieving recommendations (assuming some logic to get them)
    recommendations = Mentorship.objects.filter(alumni__email=request.GET.get('alumni_email'))
    return render(request, 'view_recommendation.html', {'recommendations': recommendations})
