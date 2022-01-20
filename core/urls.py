from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.Home, name='home'),
    path('guide/', views.Guide, name='guide'),
    path('guide_tf', views.GuideTf, name='guide_tf'),
    path('guide_tt', views.GuideTt, name='guide_tt'),
    path('amputation', views.Amputation, name='amputation'),
    path('search', views.Search, name='search'),
    path('userstory', views.UserStory, name='userstory'),
    path('admin_page', views.AdminPage, name='admin-page'),

]