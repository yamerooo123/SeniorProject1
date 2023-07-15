from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView
from django.contrib import admin
from hello.views import (
    welcome, homepage, signup, signin, aboutus, howtobuy, partnerships, contact, contact_view, user_settings, menshoes, womenshoes, signout, filtered_products, filter_products, product_page, faqpage, user_private_info_change, user_public_info_change, 
    password_change_done, edit_account_success, cart_view, women_product_page, add_to_cart, remove_from_cart, edit_quantity, thank_you_for_purchase, checkout, buy_this,  w_add_to_cart, W_buy_this)

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
    path('product-page/<int:product_id>/', product_page, name='product_page'),
    path('women-product-page/<int:product_id>/', women_product_page, name='women_product_page'),
    path('cart-view/', cart_view, name='cart_view'),
    path('faqpage/', faqpage, name="faqpage"),
    path('user-private-info-change/', user_private_info_change, name='user_private_info_change'),
    path('user-public-info-change/', user_public_info_change, name='user_public_info_change'),
    path('change-password/', PasswordChangeView.as_view(template_name='user_settings.html'), name='change_password'),
    path('password-change-done/', password_change_done, name='password_change_done'),
    path('edit-account-success/', edit_account_success, name='edit_account_success'),
    path('cart-view/<int:product_id>/', cart_view, name="cart_view"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('edit_quantity/<int:product_id>/', edit_quantity, name='edit_quantity'),
    path('thank_you_for_purchase/', thank_you_for_purchase, name='thank_you_for_purchase'),
    path('checkout/',checkout, name='checkout'),
    path('buy-this/<int:product_id>/', buy_this, name="buy_this"),
    path('w-buy-this/<int:product_id>/', W_buy_this, name="W_buy_this"),
    path('w-add-to-cart/<int:product_id>/', w_add_to_cart, name='w_add_to_cart')
]

