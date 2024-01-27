
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Eco_app.urls')),
    path('staff/',include('Eco_admin.urls')),
    path('homes/', include('Eco_home.urls')),
    path('blogs/', include('Eco_blog.urls')),

    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
