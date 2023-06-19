from django.urls import path
from hello import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

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
    path('user-settings/', views.user_settings, name="user_settings"),
    path('menshoes/', views.menshoes, name="menshoes"),
    path('womenshoes/', views.womenshoes, name="womenshoes"),
    path('filtered_products/', views.filtered_products, name="filtered_products"),
    path('product-page/', views.product_page, name="product_page"),
    path('admin/', admin.site.urls),
    path('faqpage/', views.faqpage, name="faqpage"),
    path('user-private-info-change/', views.user_private_info_change, name="user_private_info_change"),
    path('user-public-info-change/', views.user_public_info_change, name="user_public_info_change"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='user_settings.html', success_url='/user-settings/'), name='change_password'),
    path('edit-account-success/', views.edit_account_success, name="edit_account_success"),
]
   