from django.urls import path
from hello import views
from django.contrib import admin
from .decorators import unauthenticated_user
urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', unauthenticated_user(views.signup), name="signup"),
    path('signin/', views.signin, name="signin"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('howtobuy/', views.howtobuy, name="howtobuy"),
    path('partnerships/', views.partnerships, name="partnerships"),
    path('contact/', views.contact, name="contact"),
    path('contact-view/', views.contact_view, name="contact_view"),
    path('user-dashboard/', views.user_dashboard, name="user_dashboard"),
    path('user-settings/', views.user_settings, name="user_settings"),
    path('menshoes/', views.menshoes, name="menshoes"),
    path('womenshoes/', views.womenshoes, name="womenshoes"),
    path('filtered_products/', views.filtered_products, name="filtered_products"),
    path('admin/', admin.site.urls),
]