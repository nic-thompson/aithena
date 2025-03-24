from django.contrib import admin
from django.urls import path, include  # 👈 path is needed for URL patterns

from core.views import home  # 👈 if you’re using a `home` view

urlpatterns = [
    path('', include('chat.urls')),  # 👈 this will load the HTML chat page
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
]
