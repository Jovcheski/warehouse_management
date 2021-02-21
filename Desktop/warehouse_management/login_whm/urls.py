from django.urls import path
from . import views


app_name = 'login_whm'


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.user_logout, name='logout'),
    path('sign_up_success/', views.sign_up_success, name='sign_up_success'),
]

