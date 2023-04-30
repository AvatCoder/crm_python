from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Record
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
        records = Record.objects.all()
        return render(request,'homepage.html',{'record':records})


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
                try:
                    user_obj = User.objects.get(email = email)
                    messages.success(request,f'{email} already exist')
                    return redirect('register')
                except:
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email,password=password)
                    user.save()
                    user_login = authenticate(request,username=username,password=password)
                    login(request,user_login)
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

def edit_record(request,pk):
    record = Record.objects.get(pk=pk)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        zip_code = request.POST['zip_code']
        
        record.first_name = first_name
        record.last_name = last_name
        record.phone = phone_number
        record.email = email
        record.state = state
        record.city = city
        record.address = address
        record.zip_code = zip_code
        record.save()
        messages.success(request, f"{record.first_name} {record.last_name} Updated")
        return redirect('home')
    else:
        if request.user.is_authenticated:
            return render(request, 'record.html',{'record':record})
        else:
            return redirect('home')

def new_record(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        zip_code = request.POST['zip_code']
        new_record = Record.objects.create(first_name = first_name, last_name = last_name,
                                           phone = phone_number, email = email,
                                           state = state, city = city,
                                           address = address, zip_code = zip_code,)
        new_record.save()
        messages.success(request, f"{new_record.first_name} {new_record.last_name} Created")
        return redirect('home')
    else:
        return render(request, 'new_record.html')
    
def delete_record(request,pk):
    if request.method == 'POST':
        pass
    else:
        delete_record = Record.objects.get(pk = pk)
        messages.success(request, f"{delete_record.first_name} {delete_record.last_name} deleted!")
        delete_record.delete()
        return redirect('home')
        