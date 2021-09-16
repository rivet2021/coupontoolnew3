
from django.urls import path,include
from .import views
from django.http import Http404

urlpatterns = [
  path('home/', views.home,name="home"),
 # path('sms/', views.sendsms,name="sendsms"),
 # path('smsdone/', views.smsdone,name="smsdone"),
  #path('email/', views.sendemail,name="sendemail"),
 # path('emaildone/', views.emaildone,name="emaildone"),
  path('smsdatabase/', views.smsdatabase,name="smsdatabase"),
  path('smsdatabasedone/', views.smsdatabasedone,name="smsdatabasedone"),
    

    ]
