from django.urls import path
from . import views
urlpatterns = [
 path('adminindex/',views.adminindex, name='adminindex'),
 path('addrecipe/',views.addrecipe,name='addrecipe'),
 path('viewrecipe/',views.viewrecipe, name='viewrecipe'),
 path('recipe/',views.recipe, name='recipe'),
 path('edit/<int:id>/',views.edit, name='edit'),
 path('update/<int:id>/',views.update, name='update'),
 path('delete/<int:id>/',views.delete, name='delete'),
 path('message/',views.message, name='message'),
 path('adminlogin/',views.adminlogin, name='adminlogin'),
 path('rtable/',views.rtable, name='rtable'),
 path('adlogin/',views.adlogin, name='adlogin'),
 path('adminlogout/',views.adminlogout, name='adminlogout')
]
