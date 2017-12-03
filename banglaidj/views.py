from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html',{'signup_form':form})



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
