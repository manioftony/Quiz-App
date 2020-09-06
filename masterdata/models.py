from django.db import models
from django.contrib.auth.models import User
# from django.auth.contrib.models import User
# Create your models here.

ACTIVE = ((0,'Inactive'),(2,'ACTIVE'))

class Base(models.Model):
    active = models.PositiveIntegerField(choices=ACTIVE,default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def switch(self):
        self.active = {0:2,2:0}[self.active]
        self.save()
        return self.active
    class Meta:
        abstract= True

class Questiongroup(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(Base):
    user = models.ForeignKey(User,blank=True,null=True,related_name="userquestion")
    question = models.TextField()
    group = models.ForeignKey(Questiongroup)

    def __str__(self):
        return self.question

class Answer(Base):
    user = models.ForeignKey(User,blank=True,null=True,related_name="useranswer")
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    anwer_text = models.TextField()
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.anwer_text
