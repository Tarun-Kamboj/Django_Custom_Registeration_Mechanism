from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('image/', views.image_view, name='image'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
]
