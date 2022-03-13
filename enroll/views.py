from django.http import HttpResponseRedirect
from django.shortcuts import render
from sqlalchemy import true
# from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash

def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Account created successfully...")
        fm=SignUpForm()
    else:
        fm=SignUpForm()
    return render(request,'enroll/signup.html',{"form":fm})

# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request,data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"logged in successfully...")
                    return HttpResponseRedirect('/users/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/login.html',{"form":fm})
    else:
        return HttpResponseRedirect('/users/profile/')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html')
    else:
        return HttpResponseRedirect('/users/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login/')

def password_with_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/users/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
    else:
        return HttpResponseRedirect('/users/login/')
    return render(request,'enroll/passwordold.html',{'form':fm})

def password_with_reset(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/users/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
    else:
        return HttpResponseRedirect('/users/login/')
    return render(request,'enroll/passwordreset.html',{'form':fm})