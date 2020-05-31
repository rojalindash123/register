from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from .models import Status


def welcome(request):
    return render(request,'welcome.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save();
        print('user created')
        return redirect('/status/')

        # if password1 == password2:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request,"username taken")
        #         return redirect('register')
        #     elif User.objects.filter(email=email).exists():
        #         messages.info(request,'email taken')
        #         return redirect('register')
        #     else:
        #         user = User.objects.create_user(username=username, email=email, password=password1)
        #         user.save();
        #         print('user created')
        # else:
        #     print('password not matching')
        #     return redirect('/')
    else:
        return render(request, 'register.html')


def status(request):
    if request.method == 'POST':
        status = request.POST['status']
        content = Status.objects.create(status=status)
       # content=User.objects.create(status=status)
        content.save();
        return redirect('/')
    #query_results = Status.objects.all();
    #context = {'query_results': query_results}


    else:
        return render(request, 'status.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/status/')
        else:
            messages.info(request,'Invalid credential')
            return redirect('/login/')

    else:
        return render(request,'login.html');