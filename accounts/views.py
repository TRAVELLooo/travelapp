from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"User is not registered")
            return redirect('login')
    else:
        return render(request,"login.html")

def register(request):
    try:
        if request.method == "POST":
            first_name=request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"User Exists")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Exists")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                                          email=email,password=password1)
                    user.save()
                    print("User created succesfully")
            else:
                messages.info(request, "Password Not Matched")
                return redirect('register')
            return redirect('/')
        else:
            return render(request,'registration.html')
    except:
        messages.warning(request,"Fill The Values Correctly")
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


