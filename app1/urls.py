from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista1, name='vista1'),
    path('v2/', views.vista2, name='vista2'),
]