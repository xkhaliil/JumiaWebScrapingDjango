from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
]
