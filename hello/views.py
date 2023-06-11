from django.core.mail import EmailMessage
from django.core.mail import send_mail #ส่งอีเมล
from django.http import HttpResponse #รับHttp
from django.shortcuts import render #ประมวลเว็ป
from django.shortcuts import redirect #คล้ายๆ echo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt #เอาไว้อัพไฟล์
import os 

def welcome(request):
    return render(request, 'welcomepage.html')

def homepage(request):
    return render(request, 'homepage.html')



def signup(request):
    #เช็ค attribute
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        phoneno = request.POST.get('phoneno')
        
        user = User(
            name=name,
            surname=surname,
            username=username,
            password=password,
            email=email,
            birthdate=birthdate,
            phoneno=phoneno
        )
        user.save()
        
        #return redirect('homepage.html')  # Redirect to a success page after saving

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, login)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("user_dashboard")
        else:
            messages.error(request,"Invalid username or password.")



    return render(request, 'signin.html')

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