from django.urls import path
from .views import main, about, notice, notice_form, notice_show, notice_delete, recruit, recruit_form, recruit_show, sign_in,sign_out

urlpatterns = [
    path('', main, name='main'),
    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('notice/', notice, name='notice'),
    path('notice_form/', notice_form, name='notice_form'),
    path('notice/<int:id>/', notice_show, name='notice_show'),
    path('notice/<int:id>/delete', notice_delete, name='notice_delete'),
    path('recruit/', recruit, name='recruit'),
    path('recruit_form/', recruit_form, name='recruit_form'),
    path('recruit/<int:id>', recruit_show, name='recruit_show'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
]