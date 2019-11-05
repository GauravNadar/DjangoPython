from django.urls import path
from . import views

from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)
#from .views import MySignUpView

from django.contrib.auth import views as auth_views

from . import forms

urlpatterns = [

path('', views.HomePage.as_view(), name='home'),

path('display/', views.StudentDisplay.as_view(), name='create'),
path('add/', views.StudentCreate.as_view(), name='add'),

path('delete/<int:pk>', views.StudentDelete.as_view(), name='remove'),
path('edit/<int:pk>', views.StudentEdit.as_view(), name='edit'),

path('search/', views.SearchResultsView.as_view(), name='search'),
path('search_item/', views.SearchItem.as_view(), name='search_item'),

#path('sign_up/', MySignUpView.as_view(), name='sign_up'),

#path('accounts/login/', auth_views.LoginView.as_view(template_name='crud/login.html')),

#path('login/', views.Loginclass.as_view(), name='login' )

path('marks/<int:stud_id>', views.getMarks , name='marks' ),

]