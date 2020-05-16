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
    path('notice/<int:id>/edit', notice_edit, name='notice_edit'),

    path('recruit/', recruit, name='recruit'),
    path('recruit_form/', recruit_form, name='recruit_form'),
    path('recruit/<int:id>/', recruit_show, name='recruit_show'),
    path('recruit/<int:id>/comment_form/', comment_form, name='recruit_comment_form'),
    path('recruit/<int:id>/delete', recruit_delete, name='recruit_delete'),
    path('recruit/<int:id>/edit', recruit_edit, name='recruit_edit'),

    path('qna/', qna, name='qna'),
    path('qna_form/', qna_form, name='qna_form'),
    path('qna/<int:id>/', qna_show, name='qna_show'),
    path('qna/<int:id>/comment_form/', comment_form, name='qna_comment_form'),
    path('qna/<int:id>/delete', qna_delete, name='qna_delete'),
    path('qna/<int:id>/edit', qna_edit, name='qna_edit'),

    path('edu/', edu, name='edu'),
    path('edu_form/', edu_form, name='edu_form'),
    path('edu/<int:id>', edu_show, name='edu_show'),
    path('edu/<int:id>/delete', edu_delete, name='edu_delete'),
    path('edu/<int:id>/delete', edu_delete, name='edu_delete'),
    path('edu/<int:id>/edit', edu_edit, name='edu_edit'),

    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('edit_pwd/', edit_pwd, name='edit_pwd'),
]