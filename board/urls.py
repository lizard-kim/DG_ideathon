from django.urls import path
from .views import main, about, notice, notice_form, notice_show, recruit, recruit_form, recruit_show, sign_in

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('notice/', notice, name='notice'),
    path('notice_form/', notice_form, name='notice_form'),
    path('notice_show/', notice_show, name='notice_show'),
    path('recruit/', recruit, name='recruit'),
    path('recruit_form/', recruit_form, name='recruit_form'),
    path('recruit_show/', recruit_show, name='recruit_show'),
    path('sign_in/', sign_in, name='sign_in'),
]