
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # ← ajouter cette ligne
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('experience/', include('experience.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)