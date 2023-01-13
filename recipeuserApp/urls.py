from django.urls import path
from . import views
urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('recipedetails/',views.recipedetails, name='recipedetails'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('singleblog/',views.singleblog, name='singleblog'),
    path('details/<int:id>/',views.details, name='details'),
    path('adddata/',views.adddata,name='adddata'),
    path('register/',views.register, name='register'),
    path('rbdata/',views.rbdata, name='rbdata'),
    path('loginuser/',views.loginuser, name='loginuser'),
    path('login_data/',views.login_data, name='login_data'),
    path('userlogout/',views.userlogout, name='userlogout')
]