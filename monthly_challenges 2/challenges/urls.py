from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home_page"),
    path("<int:month>", views.monthly_challenges_url_number_version),
    path("<month>", views.monthly_challenges, name="month-challenge")
]


