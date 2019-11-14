from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser 
from . import models
from django.db import models

# Create your models here.
class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	pic = models.ImageField(upload_to='images/' )
	roll_no = models.IntegerField()
	gender = models.CharField(max_length=30)
	#user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


	def __str__(self):
		return "%s %s %s" % (self.name, self.roll_no, self.gender)

class Marks(models.Model):
	student = models.ForeignKey( 'Student', on_delete=models.CASCADE,)
	maths = models.IntegerField()
	science = models.IntegerField()
	english = models.IntegerField() 


# class User(AbstractUser):
# 	is_student = models.BooleanField(default=False)
# 	is_teacher = models.BooleanField(default=False)


