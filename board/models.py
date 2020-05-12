from django.db import models

class User(models.Model):
    name = models.CharField(
        max_length=20,
        default="anonymous"
    )
    birthday = models.DateField(
        auto_now=False, 
        auto_now_add=False
    )
    phonenumber = models.CharField( 
        max_length=20,
        default="no number"
    )
    school = models.CharField(
        max_length=20,
        default = "no school"
    )
    email = models.CharField(
        max_length=50,
        default = "test@gmail.com"
    )
    address = models.CharField(
        max_length=60,
        default = "address"
    )
    team = models.CharField(
        max_length=50,
        default = "team"
    )
    auth = models.CharField(
        max_length=10,
        default="user"
        #user leader judge admin
    )

    def __str__(self):
        return self.name

'''
이름
생년월일
연락처
재학중인 학교
이메일
주소
소속팀
'''