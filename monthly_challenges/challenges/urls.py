from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenges_int),
    path("<month>", views.monthly_challenges, name="month-challenge"),
    
]