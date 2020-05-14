from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Idea, Notice, Recruit, Qna, Edu

def main(request):
    return render(request, 'main.html')

def notice(request):
    notice = Notice.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'notice.html',{
            'login_user':login_user,
            'notice' : notice,
        })
    else:
        return render(request, 'notice.html',{
            'notice' : notice
        })

def about(request):
    return render(request, 'about.html')

def notice_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']

        newnotice = Notice.objects.create(
            title = title,
            contents = contents,
        )
        return redirect('../')

    else:
        return render(request, 'notice_form.html')

def notice_show(request, id):
    notice = Notice.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'notice_show.html',{
            'login_user':login_user,
            'notice' : notice,
        })
    else:
        return render(request, 'notice_show.html', {
            'notice':notice,
        })

def notice_delete(request, id):
    if request.method == 'POST':
        notice = Notice.objects.filter(id=id)
        notice.delete()
        return redirect('../')

def recruit(request):
    recruit = Recruit.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'recruit.html',{
            'login_user':login_user,
            'recruit' : recruit,
        })
    else:
        return render(request, 'recruit.html',{
            'recruit' : recruit
        })

def recruit_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newrecruit = Recruit.objects.create(
            title = title,
            contents = contents,
            writer = username,
        )
        return redirect('/recruit/')

    else:
        return render(request, 'recruit_form.html')

def recruit_show(request, id):
    recruit = Recruit.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'recruit_show.html',{
            'login_user':login_user,
            'recruit' : recruit,
        })
    else:
        return render(request, 'recruit_show.html', {
            'recruit':recruit,
        })
    return render(request, 'recruit_show.html')

def qna(request):
    qna = Qna.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'qna.html',{
            'login_user':login_user,
            'qna' : qna,
        })
    else:
        return render(request, 'qna.html',{
            'qna' : qna
        })


def qna_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newqna = Qna.objects.create(
            title = title,
            contents = contents,
            writer = username,
        )
        return redirect('/qna/')

    else:
        return render(request, 'qna_form.html')

def qna_show(request, id):
    qna = Qna.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'qna_show.html',{
            'login_user':login_user,
            'qna' : qna,
        })
    else:
        return render(request, 'qna_show.html', {
            'qna':recruit,
        })
    return render(request, 'qna_show.html')

def edu(request):
    edu = Edu.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'edu.html',{
            'login_user':login_user,
            'edu' : edu,
        })
    else:
        return render(request, 'edu.html',{
            'edu' : edu
        })

def edu_show(request, id):
    edu = Edu.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'edu_show.html',{
            'login_user':login_user,
            'edu' : edu,
        })
    else:
        return render(request, 'edu_show.html', {
            'edu':recruit,
        })
    return render(request, 'edu_show.html')

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

def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('../')
    return render(request, 'main.html')
