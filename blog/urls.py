from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/',views.me, name='blog-about'),
    path('quavo/',views.start, name='blog-quavo')
]
