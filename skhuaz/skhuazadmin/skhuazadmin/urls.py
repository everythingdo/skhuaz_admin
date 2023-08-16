from django.contrib import admin
from django.urls import path
import skhuaz_admin.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skhuaz_admin.views.index, name='index'),
]
