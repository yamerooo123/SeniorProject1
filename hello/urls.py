from django.urls import path
from hello import views
from django.contrib import admin

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('howtobuy/', views.howtobuy, name="howtobuy"),
    path('partnerships/', views.partnerships, name="partnerships"),
    path('contact/', views.contact, name="contact"),
    path('contact-view/', views.contact_view, name="contact_view"),
    path('user-dashboard/', views.user_dashboard, name="user_dashboard"),
    path('user-settings/', views.user_settings, name="user_settings"),
    path('admin/', admin.site.urls),
    
]