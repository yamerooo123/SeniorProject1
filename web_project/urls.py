"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from hello.views import welcome
from hello.views import homepage
from hello.views import signup
from hello.views import signin
from hello.views import aboutus
from hello.views import howtobuy
from hello.views import partnerships
from hello.views import contact
from hello.views import contact_view
from hello.views import user_dashboard
from hello.views import user_settings
from hello.views import menshoes
from hello.views import womenshoes
from django.contrib import admin
from hello.views import signout
from hello.views import filtered_products
from hello.views import filter_products
from hello.views import product_page
urlpatterns = [
    path('', welcome, name='welcome'),
    path('homepage/',homepage, name='homepage'),
    path('signup/',signup, name="signup"),
    path('signin/',signin, name="signin"),
    path('aboutus/',aboutus, name="aboutus"),
    path('howtobuy/',howtobuy, name="howtobuy"),
    path('partnerships/',partnerships, name="partnerships"),
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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)