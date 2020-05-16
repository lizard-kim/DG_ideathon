from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import *

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
        return redirect('/notice/')

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
        return redirect('/notice/')

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
            'qna':qna,
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

def edu_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']

        newedu = Edu.objects.create(
            title = title,
            contents = contents,
        )
        return redirect('/edu/')

    else:
        return render(request, 'edu_form.html')

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

def edu_delete(request, id):
    if request.method == 'POST':
        edu = Edu.objects.filter(id=id)
        edu.delete()
        return redirect('/edu/')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            # login success
            auth.login(request, user)
            return redirect('/main/')
        else:
            return render(request, 'sign_in.html', {'error': '* 이메일 혹은 비밀번호가 잘못되었습니다.'})
    else:
        return render(request, 'sign_in.html')

def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/main/')
    return render(request, 'main.html')

def edit_pwd(request):
    if request.method == 'POST':
        password = request.POST['password']
        new_password = request.POST['new_password']
        password_confirm = request.POST['password_confirm']
        user = request.user
        if check_password(password,user.password) and new_password == password_confirm:
            user.set_password(new_password)
            user.save()
            auth.login(request, user)
            return redirect('/main/')
        else:
            return render(request, 'edit_pwd.html', {'error': '* 잘못된 정보를 기입하셨습니다.'})
    else:
        return render(request, 'edit_pwd.html')


def comment_form(request, id):
    #print(request.path)
    path = request.path
    path = path[1:]
    #print(path)
    path_len = len(path)
    location = ""

    i = 0
    while(path[i] != "/"):
        point = path[i]
        location += point
        i += 1
    #print(location)

    if request.method == 'POST':
        contents = request.POST['contents']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newcomment = Comment.objects.create(
            contents = contents,
            writer = username,
        )
        if(location == "qna"):
            qna = Qna.objects.filter(id=id).get()      
            qna.comments.add(newcomment)
        elif(location == "recruit"):
            recruit = Recruit.objects.filter(id=id).get()      
            recruit.comments.add(newcomment)
        return redirect('../')