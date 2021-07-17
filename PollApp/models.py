from django.db import models

# Create your models here.
class Register(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	place=models.CharField(max_length=30)
	mobile=models.CharField(max_length=20)
	email=models.EmailField()
	password=models.CharField(max_length=20)

class CreatePoll(models.Model):
	register=models.ForeignKey(Register,on_delete=models.CASCADE,default='1')
	question=models.CharField(max_length=200,blank=False)
	option1=models.CharField(max_length=100,blank=False)
	option2=models.CharField(max_length=100,blank=False)
	option3=models.CharField(max_length=100,blank=False)
	option4=models.CharField(max_length=100,blank=False)
	option1_count=models.IntegerField(default=0)
	option2_count=models.IntegerField(default=0)
	option3_count=models.IntegerField(default=0)
	option4_count=models.IntegerField(default=0)




	