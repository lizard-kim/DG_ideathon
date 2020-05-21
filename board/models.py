from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
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
    attach = models.FileField(
        upload_to='attach_file', 
        blank=True, 
        null=True
    )
    def __str__(self):
        return self.title

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

class Notice(models.Model):
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

class Recruit(models.Model):
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
    writer = models.CharField(
        max_length=50,
        blank=True
    )
    job = models.CharField(
        max_length=50,
        blank=True
    )
    comments = models.ManyToManyField(
        "Comment",
        blank=True,
        related_name="recruit_comments"
    )
    def __str__(self):
        return self.title

class Qna(models.Model):
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
    writer = models.CharField(
        max_length=50,
        blank=True
    )
    comments = models.ManyToManyField(
        "Comment",
        blank=True,
        related_name="qna_comments"
    )
    def __str__(self):
        return self.title

class Edu(models.Model):
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

class Comment(models.Model):
    contents = models.TextField(
        max_length=300
    )
    date = models.DateField(
        auto_now=True, 
        auto_now_add=False
    )
    writer = models.CharField(
        max_length=50,
        blank=True
    )
    def __str__(self):
        return self.contents

class Mid(models.Model):
    title = models.CharField(
        max_length=50,
    )
    date = models.DateField(
        auto_now=True, 
        auto_now_add=False
    )
    team = models.CharField(
        max_length=50,
    )
    leader = models.CharField(
        max_length=50,
    )
    topic = models.CharField(
        max_length=10,
    )
    result = models.CharField(
        max_length=10,
    )
    writer = models.CharField(
        max_length=50,
    )
    motivation = models.TextField(
        max_length=500,
        blank=True
    ) 
    process = models.TextField(
        max_length=500,
        blank=True
    )
    expectation = models.TextField(
        max_length=500,
        blank=True
    ) 
    file = models.TextField(
        max_length=500,
    ) 
    comments = models.ManyToManyField(
        "Comment",
        blank=True,
        related_name="mid_comments"
    )
    def __str__(self):
        return self.team