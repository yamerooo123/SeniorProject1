from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import os
from .models import UserProfile, ShoeFeatures, WomenShoeFeatures, M_Cart, User
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP

def welcome(request):
    return render(request, 'welcomepage.html')


def homepage(request):
    return render(request, 'homepage.html')



@csrf_protect
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        phoneno = request.POST.get('phoneno')
        
        if password != password2:
            messages.error(request, "Sorry, passwords do not match :(")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Sorry, this username already exists :(")
        
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Sorry, this email has been registered. :(")
        
        elif UserProfile.objects.filter(phoneno=phoneno).exists():
            messages.error(request, "Sorry, this phone number has been registered. :(")
        
        else:
            user = User.objects.create_user(
                username=username,  
                password=password,
                email=email,
                first_name=name,
                last_name=surname
            )
            user_profile = UserProfile.objects.create(
                user=user,
                birthdate=birthdate,
                phoneno=phoneno
            )
            messages.success(request, "Registration is completed. You may login. ;)")
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"form": form})


def signout(request):
    logout(request)
    return redirect('homepage')
def aboutus(request):
    return render(request, 'aboutus.html')

def howtobuy(request):
    return render(request, 'howtobuy.html')

def partnerships(request):
    return render(request, 'partnerships.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        details = request.POST.get('details')
        file = request.FILES.get('file')

        if file:
            file_path = os.path.join('C:\\Users\\monaliza\\Downloads', file.name)
            with open(file_path, 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

       
        subject = f'New Contact from www.happyfeet.com: {problem}'
        message = f'Name: {name}\nEmail: {email}\nProblem: {problem}\nDetails: {details}'
        if file:
            email = EmailMessage(subject, message, 'u6311374@au.edu', ['pgrreroll100@gmail.com'])
            email.attach_file(file_path)
            email.send()
        else:
            send_mail(subject, message, 'u6311374@au.edu', ['pgrreroll100@gmail.com'])

        return redirect('/contact/?success=true')

    return render(request, 'contact.html')

def user_dashboard(request):
    return render(request, "user_dashboard.html", {'user': request.user})


def user_settings(request):
    return render(request, 'user_settings.html')

def menshoes(request):
    shoefeatures = ShoeFeatures.objects.all()
    context = {
        'shoefeatures': shoefeatures,
    }
    return render(request, 'menshoes.html', context)


def womenshoes(request):
    womenshoefeature = WomenShoeFeatures.objects.all()
    context = {
        'womenshoefeatures': womenshoefeature,
    }
    return render(request, 'womenshoes.html', context)

def product_page(request, product_id):
    shoefeature = get_object_or_404(ShoeFeatures, product_id=product_id)
    context = {
        'shoefeatures': [shoefeature],

    }
    return render(request, 'product_page.html', context)

def women_product_page(request, product_id):
    womenshoefeature = get_object_or_404(WomenShoeFeatures, product_id=product_id)
    context = {
        'womenshoefeatures': [womenshoefeature],
    }
    return render(request, 'women_product_page.html', context)

def filtered_products(request):
    return render(request, 'filtered_products.html')

def filter_products(request):
    type1 = request.GET.get('type1')  
    type2 = request.GET.get('type2') 
    maincolor = request.GET.get('maincolor')  
    subcolor = request.GET.get('subcolor')   
    size = request.GET.get('size') 
    price_range = request.GET.getlist('price_range')  
    brand = request.GET.get('brand')  
    
    
    
    if type1:
        products = products.filter(type1=type1)
    if type2:
        products = products.filter(type2=type2)
    if size:
        products = products.filter(size=size)    
    if maincolor:
        products = products.filter(maincolor=maincolor)
    if subcolor:
        products = products.filter(subcolor=subcolor)
    if price_range:
        if 'low' in price_range:
            products = products.filter(price__lte=50)  
        if 'medium' in price_range:
            products = products.filter(price__gt=50, price__lte=100)  
            products = products.filter(price__gt=100) 
    if brand:
        products = products.filter(brand=brand)
    context = {
        'filtered_products': products
    }
    return render(request, 'filtered_products.html', context)

def faqpage(request):
    return render(request, 'faqpage.html')

@login_required
@csrf_protect
def user_private_info_change(request):
    if request.method == 'POST':
        address = request.POST.get('inputAddress')
        address1 = request.POST.get('inputAddress1')
        city = request.POST.get('inputCity')
        state = request.POST.get('inputState')
        zip_code = request.POST.get('inputZip')

        if zip_code and not zip_code.isdigit():
            message = "Invalid zip code. Please enter the correct zip code."
            return render(request, "user_settings.html", {'message': message})

        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        user_profile.address = address
        user_profile.address1 = address1
        user_profile.city = city
        user_profile.state = state
        user_profile.zip_code = zip_code
        user_profile.save()

        return redirect("edit_account_success")

    return render(request, "user_settings.html")

@login_required
@csrf_protect
def user_public_info_change(request):
    if request.method == 'POST':
        phoneno = request.POST.get('inputPhoneno')

        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        user_profile.phoneno = phoneno
        user_profile.save()

        
        return render(request, "edit_account_success.html")
    return render(request, "user_settings.html")

@login_required
@csrf_protect
def user_settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user_settings#password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'user_settings.html', context)

def password_change_done(request):
    return render(request, 'password_change_done.html')

def edit_account_success(request):
    return render(request, 'edit_account_success.html')


@login_required
def cart_view(request, product_id=None):   
    products_in_cart = M_Cart.objects.filter(username=request.user.username)

    total_amount = Decimal(0)
    vat_rate = Decimal('0.07')  

    for cart_item in products_in_cart:
        subtotal = Decimal(cart_item.product_quantity) * Decimal(cart_item.product_price)
        total_amount += subtotal

    vat_amount = total_amount * vat_rate
    total_amount_vat = total_amount + vat_amount

    total_amount = total_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    vat_amount = vat_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    total_amount_vat = total_amount_vat.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    total_amount_before_vat = total_amount

    context = {
        'products_in_cart': products_in_cart,
        'total_amount': total_amount,
        'vat_amount': vat_amount,
        'total_amount_vat': total_amount_vat,
        'total_amount_before_vat': total_amount_before_vat,
    }
    return render(request, "cart_view.html", context)

@login_required
def add_to_cart(request, product_id):
    shoefeature = get_object_or_404(ShoeFeatures, product_id=product_id)
    if request.method == 'POST':
        product_quantity = request.POST.get('quantity', 1)
        main_color = request.POST.get('main_color')
        sub_color = request.POST.get('sub_color')
        product_size = request.POST.get('product_size') 
        cart = M_Cart(
            product_price=shoefeature.price,
            productName=shoefeature.productName,
            username=request.user.username,
            product_image=shoefeature.productImage,
            product_quantity=product_quantity,
            main_color =main_color,
            sub_color=sub_color,
            product_size=product_size,
        )
        cart.save()
        return redirect('product_page', product_id=product_id)

    context = {
        'shoefeatures': shoefeature,
    }
    return render(request, 'product_page.html', context)

@login_required
def buy_this(request, product_id):
    shoefeature = get_object_or_404(ShoeFeatures, product_id=product_id)
    if request.method == 'POST':
    
        product_quantity = request.POST.get('quantity', 1)
        main_color = request.POST.get('main_color', 'Black')
        sub_color = request.POST.get('sub_color' ,'Black')
        product_size = request.POST.get('product_size', 7) 
        cart = M_Cart(
            product_price=shoefeature.price,
            productName=shoefeature.productName,
            username=request.user.username,
            product_image=shoefeature.productImage,
            product_quantity=product_quantity,
            main_color =main_color,
            sub_color=sub_color,
            product_size=product_size,
        )
        cart.save()
        return redirect('cart_view', product_id=product_id)

    context = {
        'shoefeatures': shoefeature,
    }
    return render(request, 'product_page.html', context)

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(M_Cart, product_id=product_id, username=request.user.username)
    
    if request.method == 'POST':
        product.delete()
        return redirect('cart_view')
    
    context = {
        'product': product
    }
    return render(request, 'cart_view.html', context)

def edit_quantity(request, product_id):
    cart_item = get_object_or_404(M_Cart, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.product_quantity = quantity
        cart_item.save()

        return redirect('cart_view')

def thank_you_for_purchase(request):
    products_in_cart = M_Cart.objects.filter(username=request.user.username)
    total_amount = calculate_total_amount(products_in_cart)
    vat_rate = Decimal('0.07')  
    vat_amount = total_amount * vat_rate
    total_amount_vat = total_amount + vat_amount

    context = {
        'products_in_cart': products_in_cart,
        'total_amount': total_amount,
        'vat_amount': vat_amount,
        'total_amount_vat': total_amount_vat.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP),
    }
    return render(request, "thank_you_for_purchase.html", context)

def calculate_total_amount(products_in_cart):
    total_amount = 0
    for cart_item in products_in_cart:
        total_amount += cart_item.product_quantity * cart_item.product_price
    return total_amount

def calculate_total_amount_vat(products_in_cart):
    vat_rate = settings.vat_rate
    total_amount = 0
    for cart_item in products_in_cart:
        subtotal = cart_item.product_quantity * cart_item.product_price
        vat_amount = subtotal * vat_rate
        total_amount += subtotal + vat_amount
    return total_amount


def checkout(request):
    if request.method == "POST":
        order = M_Cart.objects.filter(username=request.user.username)
        if order.exists():
            order.delete()
            return redirect('thank_you_for_purchase')
        else:
           return redirect('cart_view')
    return render(request, 'cart_view.html')