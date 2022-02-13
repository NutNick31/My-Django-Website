from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('academic/', views.academic, name='blog-academic'),
    path('contact/', views.contact, name='blog-academic'),
]