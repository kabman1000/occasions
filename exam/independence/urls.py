from django.urls import path
from . import views

app_name = 'independence'
urlpatterns = [
    path('', views.index, name = 'index'),
]