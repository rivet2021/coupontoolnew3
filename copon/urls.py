
from django.urls import path,include
from .import views
from django.http import Http404

urlpatterns = [
  path('home/', views.home,name="home"),
# path('sms/', views.sendsms,name="sendsms"),
# path('smsdone/', views.smsdone,name="smsdone"),
 path('email/', views.sendemail,name="sendemail"),
 path('emaildone/', views.emaildone,name="emaildone"),
 path('smsdatabase/', views.smsdatabase,name="smsdatabase"),
 path('smsdatabasedone/', views.smsdatabasedone,name="smsdatabasedone"),
  path('whatsapp/', views.whatsapp,name="whatsapp"),
  path('whatsappdone/', views.whatsappdone,name="whatsappdone"),
  path('landingcopon/', views.landingcopon,name="landingcopon"),
  
  path('success/', views.success,name="success"),
  path('cancel/', views.cancel,name="cancel"),
  path('subscribe/', views.subscribe,name="subscribe"),
  path('subcompleted/', views.subcompleted,name="subcompleted"),
  #path('login/', views.login,name="login"),
 # path('registerattempt/', views.registerattempt,name="registerattempt"),
  path('logout_account/', views.logout_account,name="logout_account"),
  path('landing/',views.checkout,name="landing"),
  path('mainsuccess/',views.mainsuccess,name="mainsuccess"),
   path('successlanding/',views.successlanding,name="successlanding"),
   path('okay/<int:id>/',views.okay,name="okay"),
   
    path('unsubscribe/',views.unsubscribe,name="unsubscribe"),
    path('final/',views.final,name="final"),
    path('updated/',views.updated,name="updated"),
    path('signup/',views.signup,name="signup"),
    path('index/',views.index,name="index"),
    path('reg/',views.reg,name="reg"),
  
  
    
  


  

  
  
    

    ]
