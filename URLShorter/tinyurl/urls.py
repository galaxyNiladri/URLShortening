from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tiny',views.url_short,name='tiny')
]

