from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('campaigns/', include('campaigns.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('engagement.urls')),
]
