from django.urls import path
from . import views
from .views import home

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('search',views.searching,name='search'),

]