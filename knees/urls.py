from django.urls import path
from knees import views
from . import views


app_name = 'knees'

urlpatterns = [
    path('', views.Knees, name="knees"),
]