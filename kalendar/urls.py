from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret_admin_123_page/', admin.site.urls),
    path('', include('cal.urls')),
    path('', include('seznam_kontaktu.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
