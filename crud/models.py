from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	roll_no = models.IntegerField()
	gender = models.CharField(max_length=30)


	def __str__(self):
		return "%s %s %s" % (self.name, self.roll_no, self.gender)

class Marks(models.Model):
	student = models.ForeignKey( 'Student', on_delete=models.CASCADE,)
	maths = models.IntegerField()
	science = models.IntegerField()
	english = models.IntegerField() 