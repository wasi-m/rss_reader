from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:link>/', views.detail, name='detail'),
]