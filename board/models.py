from django.db import models


class Idea(models.Model):
    title = models.CharField(
        max_length=50,
    )
    date = models.DateField(
        auto_now=True, 
        auto_now_add=False
    )
    contents = models.TextField(
        max_length=500,
        blank=True
    )

    def __str__(self):
        return self.title

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
    idea = models.ForeignKey(
        Idea, 
        null=True, 
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name