from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='developer-home'),
    path('experience/', views.experience, name='developer-experience'),
]
