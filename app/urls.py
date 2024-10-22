
from django.contrib import admin
from django.urls import path
from filmes_projetc.views import home, filme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('filme/', filme, name='filme'),
]
