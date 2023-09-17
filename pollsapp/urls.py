from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index),
    path('vote/<str:pk>',views.vote),
    path('result/<str:pk>',views.result)
]