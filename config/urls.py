from django.contrib import admin
from django.urls import include, path

from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    # path('test/', admin.site.urls('jobs.urls')),

    path('test/', include('jobs.urls')), #html 및 js 공부를 위한 page

]
