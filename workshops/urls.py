from django.urls import path
from . import views

app_name = 'workshops'

urlpatterns = [
    path('', views.search, name='workshop-list'),
    path('workshops_admin_list/', views.WorkshopAdminListView.as_view(), name='workshops-admin-list'),
    path('workshops_admin_list/<int:pk>/delete', views.WorkshopAdminDeleteView.as_view(), name='workshop-admin-delete'),
    path('add/', views.WorkshopAdminCreateView.as_view(), name='workshop-admin-create'),
    path('workshops_admin_list/<int:pk>/update', views.WorkshopAdminUpdateView.as_view(), name='workshop-admin-update'),
    
]