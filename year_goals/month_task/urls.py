from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('<month>', views.month_task, name="month_url_path")
]