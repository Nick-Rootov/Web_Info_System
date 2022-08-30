from django.urls import path
from .import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.index, name='home'),
    path('sotr', views.sotr, name='sotr'),
    path('dogov', views.dogov, name='dogov'),
    path('proj', views.proj, name='proj'),
    path('add_sotr', views.add_sotr, name='add_sotr'),
    path('add_dogov', views.add_dogov, name='add_dogov'),
    path('add_proj', views.add_proj, name='add_proj'),
    path('otd', views.otd, name='otd'),
    path('mach', views.mach, name='mach'),
]
#path('sotr', cache_page(60)(views.sotr), name='sotr'),