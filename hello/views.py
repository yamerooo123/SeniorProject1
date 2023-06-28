from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import os
from .models import UserProfile, ShoeFeatures



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
    return render(request, 'menshoes.html')

def womenshoes(request):
    return render(request, 'womenshoes.html')

def product_page(request):
    return render(request, 'product_page.html')

def cart_view(request):
    return render(request, "cart_view.html")

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
    
    
    products = ShoeFeatures.objects.all() 
    
    
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


