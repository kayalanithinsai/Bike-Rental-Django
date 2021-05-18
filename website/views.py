from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth
from django.contrib.auth import login, logout

def About(request):
    return render(request, 'About.html')

def signin(request):
    if request.user.is_authenticated :
        return redirect('/')
    else:
        if request.method == 'POST':
            user_name=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=user_name,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Invalid credentials')
                return render(request,'login.html')
        else:
            return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        user_name=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        if (password==password1 and password1 != None and len(password) >= 8 ) :
            if User.objects.filter(username=user_name):
                messages.info(request,'username taken')
            else:
                user=User.objects.create_user(username=user_name , email=email, password=password, first_name=first_name, last_name=last_name )
                user.save()
                return redirect('/')
        else:
            messages.info(request,'password must be minimum 8 charecters')
            return render(request, 'register.html')
    else:
        message=''
        return render(request, 'register.html',{'message': message })
def signout(request):
    logout(request)
    return redirect('/')
