from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('home',views.home,name="home"),
   path('login',views.log,name="login"),
   path('loged',views.loged,name="loged"),
   path('reg',views.reg,name="register"),
   path('give',views.give,name="give"),
   path('adopt',views.adopt,name="adopt"),
   path('adoptcus',views.adoptcus,name="adoptcus"),
   path('vet',views.vet,name="vet"),
   path('aboutus',views.aboutus,name="aboutus"),
   path('vaccine',views.vaccine,name="vaccine"),
   path('deworm',views.deworm,name="deworm"),
   path('surgeon',views.surgeon,name="surgeon"),
   path('contact',views.contact,name="contact"),
   path('suces',views.suces,name="suces"),
   path('admin',views.admin,name="admin"),
   path('adoptsuccess',views.adoptsuccess,name="adoptsuccess")
   


]