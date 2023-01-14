from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorized/', views.AuthorizedView.as_view(), name='authorized'),
    path('search/', views.search, name='search'),
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('logout/', views.LogoutInterfaceView.as_view(), name="logout"),
]