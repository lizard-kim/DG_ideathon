from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile, Idea

def main(request):
    return render(request, 'main.html')

def notice(request):
    return render(request, 'notice.html')

def about(request):
    return render(request, 'about.html')

def notice_form(request):
    return render(request, 'notice_form.html')

def notice_show(request):
    return render(request, 'notice_show.html')

def recruit(request):
    return render(request, 'recruit.html')

def recruit_form(request):
    return render(request, 'recruit_form.html')

def recruit_show(request):
    return render(request, 'recruit_show.html')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            # login success
            auth.login(request, user)
            return redirect('../')
        else:
            return render(request, 'sign_in.html', {'error': 'email or password is incorrect.'})
    else:
        return render(request, 'sign_in.html')