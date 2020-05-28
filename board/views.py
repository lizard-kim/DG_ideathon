from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import *

def main(request):
    return render(request, 'notice.html')

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

def notice_edit(request, id):
    if request.method == 'POST':
        notice = Notice(id=id)
        title = request.POST['title']
        contents = request.POST['contents']
        notice.title = title
        notice.contents = contents
        notice.save()
        return redirect('./')

    else:
        notice = Notice.objects.filter(id=id).get()
        return render(request, 'notice_edit.html',{
            'notice' : notice
        })

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
        job = request.POST['job']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newrecruit = Recruit.objects.create(
            title = title,
            contents = contents,
            writer = username,
            job = job,
        )
        return redirect('/recruit/')

    else:
        return render(request, 'recruit_form.html')

def recruit_edit(request, id):
    if request.method == 'POST':
        recruit = Recruit(id=id)
        title = request.POST['title']
        contents = request.POST['contents']
        job = request.POST['job']
        recruit.title = title
        recruit.contents = contents
        recruit.job = job
        recruit.save()
        return redirect('./')

    else:
        recruit = Recruit.objects.filter(id=id).get()
        return render(request, 'recruit_edit.html',{
            'recruit' : recruit
        })

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

def recruit_delete(request, id):
    if request.method == 'POST':
        recruit = Recruit.objects.filter(id=id)
        recruit.delete()
        return redirect('/recruit/')

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

def qna_edit(request, id):
    if request.method == 'POST':
        qna = Qna(id=id)
        title = request.POST['title']
        contents = request.POST['contents']
        qna.title = title
        qna.contents = contents
        qna.save()
        return redirect('./')

    else:
        qna = Qna.objects.filter(id=id).get()
        return render(request, 'qna_edit.html',{
            'qna' : qna
        })

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

def qna_delete(request, id):
    if request.method == 'POST':
        qna = Qna.objects.filter(id=id)
        qna.delete()
        return redirect('/qna/')

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

def edu_edit(request, id):
    if request.method == 'POST':
        edu = Edu(id=id)
        title = request.POST['title']
        contents = request.POST['contents']
        edu.title = title
        edu.contents = contents
        edu.save()
        return redirect('./')

    else:
        edu = Edu.objects.filter(id=id).get()
        return render(request, 'edu_edit.html',{
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
        elif(location == "midterm"):
            recruit = Mid.objects.filter(id=id).get()
            recruit.comments.add(newcomment)
        return redirect('../')


def midterm(request):
    mid = Mid.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'midterm.html',{
            'login_user':login_user,
            'mid' : mid,
        })
    else:
        return render(request, 'midterm.html',{
            'mid' : mid
        })

def midterm_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        team = request.POST['team']
        leader = request.POST['leader']
        topic = request.POST['topic']
        result = request.POST['result']
        motivation = request.POST['motivation']
        process = request.POST['process']
        expectation = request.POST['expectation']
        file = request.POST['file']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newmid = Mid.objects.create(
            title = title,
            writer = username,
            team = team,
            leader = leader,
            topic = topic,
            result = result,
            motivation = motivation,
            process = process,
            expectation = expectation,
            file = file,
        )
        return redirect('/midterm/')

    else:
        return render(request, 'midterm_form.html')

def midterm_show(request, id):
    mid = Mid.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'midterm_show.html',{
            'login_user':login_user,
            'mid' : mid,
        })
    else:
        return render(request, 'midterm_show.html', {
            'mid':mid,
        })

def mid_edit(request, id):
    if request.method == 'POST':
        mid = Mid(id=id)
        title = request.POST['title']
        team = request.POST['team']
        leader = request.POST['leader']
        topic = request.POST['topic']
        result = request.POST['result']
        motivation = request.POST['motivation']
        process = request.POST['process']
        expectation = request.POST['expectation']
        file = request.POST['file']
        mid.title = title
        mid.team = team
        mid.leader = leader
        mid.topic = topic
        mid.result = result
        mid.motivation = motivation
        mid.process = process
        mid.expectation = expectation
        mid.file = file
        mid.save()
        return redirect('./')

    else:
        mid = Mid.objects.filter(id=id).get()
        return render(request, 'midterm_edit.html',{
            'mid' : mid
        })

def final(request):
    fin = Fin.objects.all()
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'final.html',{
            'login_user':login_user,
            'fin' : fin,
        })
    else:
        return render(request, 'final.html',{
            'fin' : fin
        })

def final_show(request, id):
    fin = Fin.objects.get(id=id)
    if(request.user.username):
        username = User.objects.get(username=request.user.username)
        login_user = Profile.objects.filter(email=username).get()
        return render(request, 'final_show.html',{
            'login_user':login_user,
            'fin' : fin,
        })
    else:
        return render(request, 'midterm_show.html', {
            'fin':fin,
        })

def final_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        team = request.POST['team']
        leader = request.POST['leader']
        topic = request.POST['topic']
        result = request.POST['result']
        motivation = request.POST['motivation']
        process = request.POST['process']
        expectation = request.POST['expectation']
        file = request.POST['file']
        video = request.POST['video']
        if(request.user.username):
            username = User.objects.get(username=request.user.username)
        newfin = Fin.objects.create(
            title = title,
            writer = username,
            team = team,
            leader = leader,
            topic = topic,
            result = result,
            motivation = motivation,
            process = process,
            expectation = expectation,
            file = file,
            video = video,
        )
        return redirect('/final/')

    else:
        return render(request, 'final_form.html')


def fin_edit(request, id):
    if request.method == 'POST':
        fin = Fin(id=id)
        title = request.POST['title']
        team = request.POST['team']
        leader = request.POST['leader']
        topic = request.POST['topic']
        result = request.POST['result']
        motivation = request.POST['motivation']
        process = request.POST['process']
        expectation = request.POST['expectation']
        file = request.POST['file']
        video = request.POST['video']
        fin.title = title
        fin.team = team
        fin.leader = leader
        fin.topic = topic
        fin.result = result
        fin.motivation = motivation
        fin.process = process
        fin.expectation = expectation
        fin.file = file
        fin.video = video
        fin.save()
        return redirect('./')

    else:
        fin = Fin.objects.filter(id=id).get()
        return render(request, 'final_edit.html',{
            'fin' : fin
        })
        

def poll(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        accept = request.POST['accept']
        idea_id = request.POST['idea_id']
        field = request.POST['field']

        if accept:
            pass
        else:
            return render(request, 'poll.html', {
                "error" : "약관에 동의해주세요"
            })

        if field == "bm":
            same = 0 # no
            all_voter = BM_Voter.objects.all()
            for voter in all_voter:
                if(voter.phone == phone):
                    same = 1
                    break
                else:
                    pass
            if same:
                return redirect('./')
            else:
                new_bmvoter = BM_Voter.objects.create(
                    name = name,
                    address = address,
                    phone = phone,
                    accept = accept,
                    idea_id = idea_id,
                )
        elif field == "ux":
            same = 0 # no
            all_voter = UX_Voter.objects.all()
            for voter in all_voter:
                if(voter.phone == phone):
                    same = 1
                    break
                else:
                    pass
            if same:
                return redirect('./')
            else:
                new_uxvoter = UX_Voter.objects.create(
                    name = name,
                    address = address,
                    phone = phone,
                    accept = accept,
                    idea_id = idea_id,
                )
        elif field == "sw":
            same = 0 # no
            all_voter = SW_Voter.objects.all()
            for voter in all_voter:
                if(voter.phone == phone):
                    same = 1
                    break
                else:
                    pass
            if same:
                return redirect('./')
            else:
                new_swvoter = SW_Voter.objects.create(
                    name = name,
                    address = address,
                    phone = phone,
                    accept = accept,
                    idea_id = idea_id,
                )
        return redirect('./')

    else:
        fin = Fin.objects.all()
        return render(request, 'poll.html',{
            'fin' : fin
        })

