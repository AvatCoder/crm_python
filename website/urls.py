
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('logout/',views.logout_view, name="logout"),
    path('record/<int:pk>/',views.edit_record, name="edit"),
    path('new/',views.new_record, name="new"),
    path('delete/<int:pk>',views.delete_record, name="delete"),
    
]
