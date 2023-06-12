from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import os

from .models import UserProfile


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

    messages.success(request, "Registration successful. You can now login.")
            
    
    return render(request, 'signup.html', {'messages': messages.get_messages(request)})


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
                return redirect("user_dashboard")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"form": form})

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

        # Send email
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
    return render(request, 'user_dashboard.html')


def user_settings(request):
    return render(request, 'user_settings.html')