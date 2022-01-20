from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.search, name='posts-list'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-delete",),
]