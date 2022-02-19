

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('about',views.about, name='about'),
    path('content',views.content, name='content'),
    path('contact',views.contact, name='contact'),

]
