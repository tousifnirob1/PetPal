from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html/', views.index, name='index'),
    path('pet/<int:pet_id>/', views.pet_details, name='petdetails'),
    path('pet/<int:pet_id>/confirm/', views.confirm_adoption, name='confirm_adoption'),
    path('caregiver/<int:caregiver_id>/', views.giver_details, name='cgdetails'),
    path('cgdetails.html/', views.giver_details_static, name='cgdetails_static'), 
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('add_caregiver/', views.add_caregiver, name='add_caregiver'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]