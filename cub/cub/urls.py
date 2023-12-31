from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('calendars/', include('calendars.urls')),
    path('bot/', include('bot.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
