from django.urls import path

from myapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('loginUser', views.loginUser, name='loginUser')
]

