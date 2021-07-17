from django.shortcuts import render,redirect
from .models import Register,CreatePoll
from .forms import RegisterForm,LoginForm,PollForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request,'index.html')

#To register the user
def register(request):
	if request.method=="POST":
		reg=RegisterForm(request.POST or None)
		if reg.is_valid():
			userReg=Register()
			userReg.name=reg.cleaned_data['Name']
			userReg.age=reg.cleaned_data['Age']
			userReg.place=reg.cleaned_data['Place']
			userReg.mobile=reg.cleaned_data['Mobile']
			userReg.email=reg.cleaned_data['Email']
			userReg.password=reg.cleaned_data['Password']
			confirmPassword=reg.cleaned_data['ConfirmPassword']
			user=Register.objects.filter(email=userReg.email).exists()
			if user:
				messages.error(request,"Email already exists")
				regForm=RegisterForm(request.POST)
				return render(request,'register.html',{'regForm':regForm})
			elif userReg.password!=confirmPassword:
				messages.error(request,"Password doesnot match")
				regForm=RegisterForm(request.POST)
				return render(request,'register.html',{'regForm':regForm})
			else:
				userReg.save()
				messages.success(request,"Registered Successfully")
				return redirect('/')

	else:
		regForm=RegisterForm()
	return render(request,'register.html',{'regForm':regForm})

#to login for the registered users
def login(request):
	if request.method=="POST":
		logForm=LoginForm(request.POST or None)
		if logForm.is_valid():
			email=logForm.cleaned_data['Email']
			password=logForm.cleaned_data['Password']
			userval=Register.objects.filter(email=email).exists()
			if not userval:
				messages.error(request,"User does not exist.Please Register!")
				logForm=LoginForm(request.POST or None)
				return render(request,'login.html',{'logForm':logForm})
			userval=Register.objects.get(email=email)
			if password!=userval.password:
				messages.error(request,"Password incorrect!")
				logForm=LoginForm(request.POST or None)
				return render(request,'login.html',{'logForm':logForm})
			else:
				request.session['user']=userval.id
				messages.success(request,"Login Successful")
				return redirect('/home/%s' %userval.id)
	else:
		logForm=LoginForm()
		return render(request,'login.html',{'logForm':logForm})

#Homepage for all logged in registers
def home(request,id):
	if request.session.has_key('user'):
		user=request.session['user']
		log=Register.objects.get(id=user)
		print(log)
		return render(request,'home.html',{'log':log})

#to create a poll
def createPoll(request,id):
	if request.session.has_key('user'):
		user=request.session['user']
		log=Register.objects.get(id=user)
	else:
		logForm=LoginForm()
		return render(request,'login.html',{'logForm':logForm})
	totalPoll=len(CreatePoll.objects.filter(register=user))
	print(totalPoll)
	if totalPoll>=5:
		messages.error(request,'A user can create only 5 polls')
		return redirect('home/')
	if request.method=="POST":
		poll=PollForm(request.POST)
		if poll.is_valid():
			pollSave=CreatePoll()
			pollSave.register=Register.objects.get(id=user)
			pollSave.question=poll.cleaned_data['Question']
			pollSave.option1=poll.cleaned_data['Option1']
			pollSave.option2=poll.cleaned_data['Option2']
			pollSave.option3=poll.cleaned_data['Option3']
			pollSave.option4=poll.cleaned_data['Option4']
			pollSave.save()
			return redirect('home/')
	else:
		poll=PollForm()
	return render(request,'createPoll.html',{'poll':poll,'log':log})

#to display all the created polls by all users
def displayPoll(request,id):
	if request.session.has_key('user'):
		user=request.session['user']
	polls=CreatePoll.objects.all()
	return render(request,'displayPoll.html',{'polls':polls})

#view a particular poll and vote
def viewPoll(request,id):
	if request.session.has_key('user'):
		user=request.session['user']
	poll=CreatePoll.objects.get(id=id)
	if request.method=="POST":
		select_option=request.POST['poll']
		if select_option=="option1":
			poll.option1_count+=1
		elif select_option=="option2":
			poll.option2_count+=1
		elif select_option=="option3":
			poll.option3_count+=1
		elif select_option=="option4":
			poll.option4_count+=1
		else:
			return HttpResponse(400,"invalid option")
		poll.save()
		messages.success(request,"Voted succesfully")
		return redirect("home/")
	return render(request,'viewPoll.html',{'poll':poll})

#view the result of a poll
def viewResult(request,id):
	result=CreatePoll.objects.get(id=id)
	return render(request,'viewResult.html',{'result':result})

#to view our profile after logging in and view the questions created by us.
def viewProfile(request,id):
	if request.session.has_key('user'):
		user=request.session['user']
		polls=CreatePoll.objects.filter(register=user)
		profile=Register.objects.get(id=user)
	else:
		logForm=LoginForm()
		return render(request,'login.html',{'logForm':logForm})
	return render(request,'viewProfile.html',{'polls':polls,'profile':profile})

#to logout from a session
def logout(request):
	if request.session.has_key('user'):
		try:
			del request.session['user']
			return redirect('')
		except:
			pass
	else:
		pass
	return render(request,'index.html')

			