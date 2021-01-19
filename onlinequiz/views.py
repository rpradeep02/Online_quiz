from django.shortcuts import render, redirect
from .models import *
# from onlinequiz.models import Exam
from django.http import HttpResponse,JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import quizform, CreateUserForm
#from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
                

        context = {'form' :form}
        # 	context = {'form':form}
        return render(request, 'register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
            return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
def index(request):
    results = Exam.objects.all()
    # if request.method == 'POST':
    #     new_question = Exam(
    #         Question =  request.POST['Question'],
    #         Option1 = request.POST['Option1'],
    #         Option2 = request.POST['Option2'],
    #         Option3 = request.POST['Option3'],
    #         Option4 = request.POST['Option4'],
    #         Correctans = request.POST['Correctans'],
    #     )
    #     new_question.save()
    return render(request,'index.html', {'results':results})

# def Score(request):
#     return render(request,'score.html')