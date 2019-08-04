from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('W<int:id>', views.view_wiki, name='view_wiki')
]
