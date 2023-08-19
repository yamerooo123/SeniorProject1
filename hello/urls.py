from django.urls import path, include
from hello import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
    path('product-page/<int:product_id>/', views.product_page, name="product_page"),
    path('women-product-page/<int:product_id>/', views.women_product_page, name="women_product_page"),
    path('admin/', admin.site.urls),
    path('faqpage/', views.faqpage, name="faqpage"),
    path('user-private-info-change/', views.user_private_info_change, name="user_private_info_change"),
    path('user-public-info-change/', views.user_public_info_change, name="user_public_info_change"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='user_settings.html', success_url='/user-settings/'), name='change_password'),
    path('edit-account-success/', views.edit_account_success, name="edit_account_success"),
    path('cart-view/<int:product_id>/', views.cart_view, name="cart_view"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('edit_quantity/<int:product_id>/', views.edit_quantity, name='edit_quantity'),
    path('w_edit_quantity/<int:product_id>/', views.w_edit_quantity, name='w_edit_quantity'),
    path('thank-you-for-purchase/', views.thank_you_for_purchase, name='thank_you_for_purchase'),
    path('checkout/', views.checkout, name='checkout'),
    path('buy-this/<int:product_id>/', views.W_buy_this, name="buy_this"),
    path('w-buy-this/<int:product_id>/', views.W_buy_this, name="W_buy_this"),
    path('w-add-to-cart/<int:product_id>/', views.w_add_to_cart, name='w_add_to_cart'),
    path('out-of-stock/', views.out_of_stock, name='out_of_stock'),
    path('search-view/', views.search_view, name="search_view"),
    path('wishlist/', views.wishlist, name='wishlist'),
]

admin.site.site_header = "Happy Feet Management System"
admin.site.site_title = "Happy Feet Management System"
admin.site.index_title = "Welcome to admin dashboard"
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)