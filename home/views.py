from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages, auth


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home:home')
        else:
            messages.info(request,'User is invalid')
            return redirect('home:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('home:register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Mail-id is already taken')
                return redirect('home:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('home:login')
        else:
            messages.info(request, 'Password is not match')
            return redirect('home:register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('home:home')