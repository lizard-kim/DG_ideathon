from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='about'),
    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('notice/', notice, name='notice'),
    path('notice_form/', notice_form, name='notice_form'),
    path('notice/<int:id>/', notice_show, name='notice_show'),
    path('notice/<int:id>/delete', notice_delete, name='notice_delete'),
    path('recruit/', recruit, name='recruit'),
    path('recruit_form/', recruit_form, name='recruit_form'),
    path('recruit/<int:id>', recruit_show, name='recruit_show'),
    path('qna/', qna, name='qna'),
    path('qna_form/', qna_form, name='qna_form'),
    path('qna/<int:id>', qna_show, name='qna_show'),
    path('edu/', edu, name='edu'),
    #path('edu_form/', edu_form, name='edu_form'),
    path('edu/<int:id>', edu_show, name='edu_show'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
]