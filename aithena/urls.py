from django.contrib import admin
from django.urls import path, include  # 👈 path is needed for URL patterns

from core.views import home  # 👈 if you’re using a `home` view

urlpatterns = [
    path('', home, name='home'),  # 👈 this handles the root URL
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
]
