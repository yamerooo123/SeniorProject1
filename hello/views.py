from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from .models import UserProfile, ShoeFeatures, WomenShoeFeatures, M_Cart, User, W_Cart, OrderTransaction
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP
from itertools import chain
from recommendation import *

def welcome(request):
    return render(request, 'welcomepage.html')


def homepage(request):
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items':total_items
    }
    return render(request, 'homepage.html', context)



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
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items': total_items,
    }

    return render(request, 'aboutus.html', context)

def howtobuy(request):
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items': total_items,
    }
    return render(request, 'howtobuy.html', context)

def partnerships(request):
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items': total_items,
    }
    return render(request, 'partnerships.html', context)

def contact(request):
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items': total_items
    }
    return render(request, 'contact.html', context)

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


def menshoes(request):
    total_items = calculate_total_items(request.user.username)
    shoefeatures = ShoeFeatures.objects.all()

    items_per_page = 10
    paginator = Paginator(shoefeatures, items_per_page)
    page_number = request.GET.get('page')
    shoefeatures_page = paginator.get_page(page_number)

    context = {
        'shoefeatures': shoefeatures_page, 
        'total_items': total_items,
    }
    return render(request, 'menshoes.html', context)


def womenshoes(request):
    total_items = calculate_total_items(request.user.username)
    womenshoefeature = WomenShoeFeatures.objects.all()
    context = {
        'womenshoefeatures': womenshoefeature,
        'total_items': total_items,
    }
    return render(request, 'womenshoes.html', context)


def product_page(request, product_id):
    total_items = calculate_total_items(request.user.username)
    shoefeature = get_object_or_404(ShoeFeatures, product_id=product_id)
    context = {
        'shoefeatures': [shoefeature],
        'total_items': total_items,

    }
    return render(request, 'product_page.html', context)

def women_product_page(request, product_id):
    total_items = calculate_total_items(request.user.username)
    womenshoefeature = get_object_or_404(WomenShoeFeatures, product_id=product_id)

    shoes_input = womenshoefeature.productName
   
    similar_shoes_list = get_similar_shoes(shoes_input, cosine_sim, shoes_dataset)

    context = {
        'womenshoefeatures': [womenshoefeature],
        'total_items': total_items,
        'similar_shoes_list': similar_shoes_list,  
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
    total_items = calculate_total_items(request.user.username)
    context = {
        'total_items': total_items,
    }
    return render(request, 'faqpage.html', context)

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
def user_settings(request):
    total_items = calculate_total_items(request.user.username)
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

    order_transactions = OrderTransaction.objects.filter(username=request.user.username, delivery_status='Ongoing')
    order_history = OrderTransaction.objects.filter(username=request.user.username, delivery_status__in=['Delivered', 'Cancelled'])

    if order_transactions.exists() and order_history.exists():
        for transaction in order_transactions:
            if transaction.delivery_status in ['Delivered', 'Cancelled']:
                order_history.create(
                    product_id=transaction.product_id,
                    username=transaction.username,
                    productName=transaction.productName,
                    product_price=transaction.product_price,
                    product_quantity=transaction.product_quantity,
                    product_image=transaction.product_image,
                    main_color=transaction.main_color,
                    sub_color=transaction.sub_color,
                    product_size=transaction.product_size,
                    payment_method=transaction.payment_method,
                    delivery_status=transaction.delivery_status,
                    total_amount_vat=transaction.total_amount_vat,
                )
                transaction.delete()

        order_transactions = OrderTransaction.objects.filter(username=request.user.username, delivery_status='Ongoing')
        order_history = OrderTransaction.objects.filter(username=request.user.username, delivery_status__in=['Delivered', 'Cancelled'])

    context = {
        'form': form,
        'order_transactions': order_transactions,
        'order_history': order_history,
        'total_items': total_items,
    }

    return render(request, 'user_settings.html', context)




def password_change_done(request):
    return render(request, 'password_change_done.html')

def edit_account_success(request):
    return render(request, 'edit_account_success.html')


@login_required
def cart_view(request, product_id=None):
    products_in_cart = M_Cart.objects.filter(username=request.user.username)
    women_products_in_cart = W_Cart.objects.filter(username=request.user.username)

    total_amount = Decimal(0)
    vat_rate = Decimal('0.07')

    for cart_item in products_in_cart:
        subtotal = Decimal(cart_item.product_quantity) * Decimal(cart_item.product_price)
        total_amount += subtotal

    for cart_item in women_products_in_cart:
        subtotal = Decimal(cart_item.product_quantity) * Decimal(cart_item.product_price)
        total_amount += subtotal

    vat_amount = total_amount * vat_rate
    total_amount_vat = total_amount + vat_amount

    total_amount = total_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    vat_amount = vat_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    total_amount_vat = total_amount_vat.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    total_amount_before_vat = total_amount
    total_items = len(women_products_in_cart) + len(products_in_cart)
    shoefeature = ShoeFeatures.objects.filter(product_id__in=[cart_item.product_id for cart_item in products_in_cart])
    w_shoefeature = ShoeFeatures.objects.filter(product_id__in=[cart_item.product_id for cart_item in women_products_in_cart])

    context = {
        'products_in_cart': products_in_cart,
        'women_products_in_cart': women_products_in_cart,
        'total_amount': total_amount,
        'vat_amount': vat_amount,
        'total_amount_vat': total_amount_vat,
        'total_amount_before_vat': total_amount_before_vat,
        'total_items': total_items,
        'shoefeature': shoefeature,
        'w_shoefeature': w_shoefeature,
    }
    return render(request, "cart_view.html", context)

def calculate_total_items(username):
    products_in_cart = M_Cart.objects.filter(username=username)
    women_products_in_cart = W_Cart.objects.filter(username=username)
    total_items = len(women_products_in_cart) + len(products_in_cart)
    return total_items

@login_required(login_url='/signin/')
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

@login_required(login_url='/signin/')
def w_add_to_cart(request, product_id):
    shoefeature = get_object_or_404(WomenShoeFeatures, product_id=product_id)
    if request.method == 'POST':
        product_quantity = request.POST.get('quantity', 1)
        main_color = request.POST.get('main_color')
        sub_color = request.POST.get('sub_color')
        product_size = request.POST.get('product_size') 
        cart = W_Cart(
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
        return redirect('women_product_page', product_id=product_id)

    context = {
        'womenshoefeatures': shoefeature,
    }
    return render(request, 'women_product_page.html', context)

@login_required(login_url='/signin/')
def buy_this(request, product_id):
    shoefeature = get_object_or_404(ShoeFeatures, product_id=product_id)
    if request.method == 'POST':
    
        product_quantity = request.POST.get('quantity', 1)
        main_color = request.POST.get('main_color', 'Black')
        sub_color = request.POST.get('sub_color', 'Black')
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
    return render(request, 'cart_view.html', context)

@login_required(login_url='/signin/')
def W_buy_this(request, product_id):
    womenshoefeature = get_object_or_404(WomenShoeFeatures, product_id=product_id)
    if request.method == 'POST':
    
        product_quantity = request.POST.get('quantity', 1)
        main_color = request.POST.get('main_color', 'Black')
        sub_color = request.POST.get('sub_color', 'Black')
        product_size = request.POST.get('product_size', 7) 
        cart = W_Cart(
            product_price=womenshoefeature.price,
            productName=womenshoefeature.productName,
            username=request.user.username,
            product_image=womenshoefeature.productImage,
            product_quantity=product_quantity,
            main_color =main_color,
            sub_color=sub_color,
            product_size=product_size,
        )
        cart.save()
        return redirect('cart_view', product_id=product_id)

    context = {
        'womenshoefeatures': womenshoefeature,
    }
    return render(request, 'cart_view.html', context)

def remove_from_cart(request, product_id):
    try:
        product = M_Cart.objects.get(product_id=product_id, username=request.user.username)
        product.delete()
    except M_Cart.DoesNotExist:
        pass
    
    try:
        w_product = W_Cart.objects.get(product_id=product_id, username=request.user.username)
        w_product.delete()
    except W_Cart.DoesNotExist:
        pass

    return redirect('cart_view')



def edit_quantity(request, product_id):
    cart_item = get_object_or_404(M_Cart, product_id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.product_quantity = quantity
        cart_item.save()
        return redirect('cart_view')

def w_edit_quantity(request, product_id):
    cart_item = get_object_or_404(W_Cart, product_id=product_id)

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
        'vat_amount': vat_amount
    }
    return render(request, "thank_you_for_purchase.html", context)

def out_of_stock(request):
    return render(request, "out_of_stock.html")

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

@login_required
def checkout(request):
    if request.method == "POST":
        username = request.user.username
        payment_method = request.POST.get('paymentMethod')

        if M_Cart.objects.filter(username=username).exists() or W_Cart.objects.filter(username=username).exists():        
            m_cart_entries = M_Cart.objects.filter(username=username)
            w_cart_entries = W_Cart.objects.filter(username=username)
            total_amount = Decimal(0)
            vat_rate = Decimal('0.07')
            for m_cart_entry in m_cart_entries:
                subtotal = Decimal(m_cart_entry.product_quantity) * Decimal(m_cart_entry.product_price)
                total_amount += subtotal
                m_product = ShoeFeatures.objects.get(productName=m_cart_entry.productName)
                if m_product.InStock >= m_cart_entry.product_quantity:
                    m_product.InStock -= m_cart_entry.product_quantity
                    m_product.save()
                else:
                    return redirect('out_of_stock')
            for w_cart_entry in w_cart_entries:
                subtotal = Decimal(w_cart_entry.product_quantity) * Decimal(w_cart_entry.product_price)
                total_amount += subtotal
                w_product = WomenShoeFeatures.objects.get(productName=w_cart_entry.productName)
                if w_product.InStock >= w_cart_entry.product_quantity:
                    w_product.InStock -= w_cart_entry.product_quantity
                    w_product.save()
                else:
                    return redirect('out_of_stock')


            vat_amount = total_amount * vat_rate
            total_amount_vat = total_amount + vat_amount

            total_amount_vat = total_amount_vat.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

            for m_cart_entry in m_cart_entries:
                OrderTransaction.objects.create(
                    product_price=m_cart_entry.product_price,
                    productName=m_cart_entry.productName,
                    username=username,
                    product_image=m_cart_entry.product_image,
                    product_quantity=m_cart_entry.product_quantity,
                    main_color=m_cart_entry.main_color,  
                    sub_color=m_cart_entry.sub_color,
                    product_size=m_cart_entry.product_size,
                    total_amount_vat=total_amount_vat,
                    payment_method=payment_method,
                )

            for w_cart_entry in w_cart_entries:
                OrderTransaction.objects.create(
                    product_price=w_cart_entry.product_price,
                    productName=w_cart_entry.productName,
                    username=username,
                    product_image=w_cart_entry.product_image,
                    product_quantity=w_cart_entry.product_quantity,
                    main_color=w_cart_entry.main_color,  
                    sub_color=w_cart_entry.sub_color,
                    product_size=w_cart_entry.product_size,
                    total_amount_vat=total_amount_vat,
                    payment_method=payment_method,
                )

            m_cart_entries.delete()
            w_cart_entries.delete()

            return redirect('thank_you_for_purchase')

    return redirect('cart_view')

def search_view(request):
    total_items = calculate_total_items(request.user.username)
    shoefeatures = ShoeFeatures.objects.all()
    womenshoefeatures = WomenShoeFeatures.objects.all() 
    search_items = request.POST.get('Search')
    if search_items:
        shoefeatures = shoefeatures.filter(productName__icontains=search_items)
        womenshoefeatures = womenshoefeatures.filter(productName__icontains=search_items)
        products = list(chain(shoefeatures, womenshoefeatures))
    else:
        products = list(chain(shoefeatures, womenshoefeatures))
        products.sort(key=lambda x: x.product_id, reverse=True)
    if not products:
        message = "Sorry, we coulnd't find the product that you want."
    else:
        message = None

    context = {
        'shoefeatures': shoefeatures,
        'womenshoefeatures': womenshoefeatures,
        'products': products,
        'total_items':total_items,
        'message': message,
    }

    return render(request, "search_results.html", context)


        