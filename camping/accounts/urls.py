from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup/home', include('home.urls')),
    path('signup/site', include('home.urls')),
    path('signup/review', include('home.urls')),
    path('login/home', include('home.urls')),
    path('login/site', include('home.urls')),
    path('login/review', include('home.urls')),
    path('login/login', include('home.urls')),
]
