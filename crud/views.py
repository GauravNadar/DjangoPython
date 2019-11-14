from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from . models import Student, Marks
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
#from .filters import StudentFilter
# Create your views here.
from django.views import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from . forms import LoginForm

from django.views.generic.edit import FormView

from django.contrib.auth.models import User


from .forms import AddForm, EditForm 


class HomePage(ListView):
	"""docstring for HomePage"""
	model = Student
	template_name = 'crud/base.html'   
	paginate_by = 3
		


class StudentCreate(CreateView):
    model = Student
    #fields = ['name', 'pic', 'roll_no', 'gender']
    form_class = AddForm
    template_name = 'crud/student_create.html'
    success_url = reverse_lazy('create')


class StudentDisplay(LoginRequiredMixin, ListView):

	login_url = 'accounts/login/'
	model = Student
	template_name = 'crud/student_form.html'   


class StudentDelete(DeleteView):
    model = Student
    template_name = 'crud/student_delete_confirmation.html'
    success_url = reverse_lazy('create' )


class StudentEdit(UpdateView):
    model = Student
    form_class = EditForm
   
    template_name = 'crud/student_edit.html'
    success_url = reverse_lazy('create')    


class SearchResultsView(ListView):
    model = Marks
    template_name = 'search_list.html'
   # queryset = Student.objects.filter(name__icontains='gaurav')


    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Student.objects.filter(name__icontains=query
           # Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


class SearchItem(ListView):
    model = Student
    template_name = 'crud/student_search.html'   


# class StudentLogin(LoginView):
# 	form_class = StudentLogin()
# 	template_name = 'home.html'   

class Loginclass(FormView):
    form_class = LoginForm
    template_name = 'crud/login.html'
    #success_url = 


def get(self, request, *args, **kwargs):
    	form = self.form_class()
    	return render(request, self.template_name, {'form': form})


# def post(self, request, *args, **kwargs):
#     form = self.form_class(request.POST)
#     if form.is_valid():
#             # <process form cleaned data>
#        u = User.objects.create_user(
#                 form.cleaned_data.get('username'),
#                 '',# request.POST['email'],
#                 form.cleaned_data.get('password1'),
#                 is_active = True
#        )
#             # TODO Display message and redirect to login
#        return HttpResponseRedirect('/accounts/login/?next=/')
#     return render(request, self.template_name, {'form': form})



def Login(View):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        #success_url = reverse_lazy('create') 
    else:
        # Return an 'invalid login' error message.
        ...







def getMarks(request, stud_id):

	from django.template import RequestContext
	from django.shortcuts import render_to_response

	context = RequestContext(request)

	student_identity = stud_id

	context_dict = {'st_id': student_identity}

	try:
		Id = Student.objects.get(student_id=student_identity)

		marks = Marks.objects.filter(student = Id)
		context_dict['marks'] = marks
		context_dict['student'] = Id
	except Student.DoesNotExist:
	
		pass

	return render_to_response('mark_show.html', context_dict, context)		




def login(request):
    m = User.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")




class RegisterStudent(CreateView):
	template_name = ""
	form_class = UserCreationForm
	success_url = reverse_lazy('')       

