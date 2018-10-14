from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm


def hello(request, name):
    msg = "Hello {}, how are you?".format(name)
    return HttpResponse(msg)


def show_page(request, page_no):
    msg = "Page No: {}".format(page_no)
    return HttpResponse(msg)


def user_signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html',{'signup_form':form})


# store demo users data
user = {
    'user_name': 'harun',
    'password': 'password123'
}


def check_user(request, username, password):
    if user['user_name'] == username:
        if user['password'] == password:
            return HttpResponse("Logged in successfully")
        else:
            return HttpResponse("Incorrect password! Try again.")
    else:
        return HttpResponse("Invalid username")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def home(request):
    return render(request, 'home.html')
