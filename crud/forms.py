from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Student


class UserRegisterForm(UserCreationForm):
	class meta:
		model=User
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control ','placeholder':'Username'})
		self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Enter Password'})
		self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Confirm Password'})


class LoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields ='__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control ','placeholder':'Username'})
		self.fields['password'].widget.attrs.update({'class': 'form-control','placeholder':'Enter Password'})



class AddForm(forms.ModelForm):

		class Meta:
			model = Student
			fields = ['name', 'pic', 'roll_no', 'gender']


class EditForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'pic', 'roll_no', 'gender']