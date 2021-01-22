from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('account/create/', views.createUserView, name='signup'),
        path('account/login/', views.loginView, name='login'),
        path('account/signout/', views.signoutView, name='signout'),
        path('account/create_message/', views.createMessageView, name='create_message'),
        path('account/mychat/', views.createMessageView, name='mychat'),
]
