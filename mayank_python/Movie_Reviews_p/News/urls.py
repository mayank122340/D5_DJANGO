from django.urls import path
from . import views

urlpatterns=[
    path('',views.News1,name="news"),
]