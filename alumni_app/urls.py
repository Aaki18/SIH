from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('success_stories/', views.success_stories, name='success_stories'),
    path('offer_mentorship/', views.offer_mentorship, name='offer_mentorship'),
    path('view_recommendation/', views.view_recommendation, name='view_recommendation'),
    path('alumni/', views.alumni_list, name='alumni_list'),
]
