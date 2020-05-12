from django.shortcuts import render

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
    return render(request, 'sign_in.html')