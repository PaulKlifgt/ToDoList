from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

from task_manager.views import error_404, error_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_manager.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

handler404 = error_404
handler500 = error_500