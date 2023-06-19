from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from django.contrib import admin
from hello.views import (
    welcome, homepage, signup, signin, aboutus, howtobuy, partnerships, contact, contact_view, user_settings, menshoes, womenshoes, signout, filtered_products, filter_products, product_page, faqpage, user_private_info_change, user_public_info_change, password_change_done
, edit_account_success
)

urlpatterns = [
    path('', welcome, name='welcome'),
    path('homepage/', homepage, name='homepage'),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('aboutus/', aboutus, name="aboutus"),
    path('howtobuy/', howtobuy, name="howtobuy"),
    path('partnerships/', partnerships, name="partnerships"),
    path('contact/', contact, name="contact"),
    path('contact-view/', contact_view, name='contact_view'),
    path('user-settings/', user_settings, name="user_settings"),
    path('menshoes/', menshoes, name='menshoes'),
    path('womenshoes/', womenshoes, name='womenshoes'),
    path('admin/', admin.site.urls),
    path('signout/', signout, name='signout'),
    path('filtered-products/', filtered_products, name='filtered_products'),
    path('filter-products/', filter_products, name='filter_products'),
    path('product-page/', product_page, name='product_page'),
    path('faqpage/', faqpage, name="faqpage"),
    path('user-private-info-change/', user_private_info_change, name='user_private_info_change'),
    path('user-public-info-change/', user_public_info_change, name='user_public_info_change'),
    path('change-password/', PasswordChangeView.as_view(template_name='user_settings.html'), name='change_password'),
    path('password-change-done/', password_change_done, name='password_change_done'),
    path('edit-account-success/', edit_account_success, name='edit_account_success'),
]   
