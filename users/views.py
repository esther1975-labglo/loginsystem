from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from users.forms import CustomUserCreationForm 
from users import forms

def dashboard(request):
    return render(request, "dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def login_page(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect(reverse('/dashboard'))
    else:
        message = "invalid password"
    return render(request, "login_page.html", {"message": message})
    
def logout_view(request):
	logout(request)
	return redirect("/dashboard")
	       
def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		username = 	request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			messages.info(request, f"logged in")
			return HttpResponse("welcome")
		else:
			messages.error(request,"Invalid username or password")
	else:    
		form = AuthenticationForm(request, data = request.POST)
	return render(request = request, template_name="login_page.html", context={"login_form":form})
	
def user_login(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         try:
        	 user = Users.objects.get(username = username, password = password)
        	 if user is not None:               
        	     return render(request, 'dashboard.html', {})
        	 else:
        	     print("Someone tried to login and failed.")
        	     print("They used username: {} and password: {}".format(username,password))
        	     return redirect('/')
         except Exception as identifier:
             return redirect('/')
     else:
          return render(request, 'login_page.html')	
     
    
    
##def loginpage(request):
##    if request.method == "GET":
##        return render(
##            request, "login_page.html",
##            {"form": LoginForm}
##        )
##    elif request.method == "POST":
##        form = LoginForm(request.POST)
##        if form.is_valid():
##            user = form.save()
##            login(request, user)
##            return redirect(reverse("dashboard"))  
##            
##def login(request):
##	user_name_QS = request.POST.get("username")
##	password_QS =  request.POST.get("password")
##	if user_name_QS is None or password_QS is None:
##		user_name_QS = "admin"
##		password_QS = "esther@123"
##	else:
##		mydict = User.objects.get(username = user_name_QS)
##		if mydict.password == password_QS:
##			return render(request, "dashboard.html")
##		else:
##			messages.error(request,'username or password not correct')	
##			return("register.html")
##		
##	return render(request,"login.html")
##
##def Login(request):
##    if request.method == 'POST':
##        username = request.POST['username']
##        password = request.POST['password']
##        user = authenticate(request, username = username, password = password)
##        if user is not None:
##            form = login(request, user)
##            messages.success(request, f' welcome {username} !!')
##            return redirect('dashboard')
##        else:
##            messages.info(request, f'account done not exit plz sign in')
##    form = AuthenticationForm()
##    return render(request, 'user/login.html', {'form':form})  
##    
##def login_user(request):
##    logout(request)
##    username = password = ''
##    if request.POST:
##        username = request.POST.get('username')
##        password = request.POST.get('password')
##
##        user = authenticate(username = username, password = password)
##        if user is not None:
##            if user.is_active:
##                login(request, user)
##                return HttpResponseRedirect('/dashboard/')
##    return render(request, 'login.html')#context_instance = RequestContext(request))                 
##  
def welcome(request):
	return render(request, "wel.html")
