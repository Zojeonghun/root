from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('feets/', include('feets.urls', namespace='feets')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('workshops/', include('workshops.urls', namespace='workshops')),
    path('knees/', include('knees.urls', namespace='knees')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)