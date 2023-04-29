from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        username = username.capitalize()
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "Username or Password incorect ")
            return redirect('home')
    else:
        
        return render(request,'homepage.html',{})


def register(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        username = username.capitalize()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        
        try:
            User.objects.get(username=username)
            messages.success(request,f"{username} is exist")
            return redirect('register')
        except:
            if password == password_2:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email,password=password)
                user.save()
                return redirect('home')
            else:
                messages.success(request,'passwords are not be match')
                return render(request,'register.html')
    else:
        return render(request,'register.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You are logout ....")
    return redirect('home')