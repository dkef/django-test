from django.urls import path, include
from hardware import views

urlpatterns = [
    path('', views.niko, name='hardware_index'),
    path('niko', views.niko, name='niko'),
]
