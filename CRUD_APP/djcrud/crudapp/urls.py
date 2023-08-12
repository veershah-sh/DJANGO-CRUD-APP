from django.urls import path
from crudapp import views

urlpatterns = [
    path('', views.index, name="home"),
]