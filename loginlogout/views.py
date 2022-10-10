from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from loginlogout.models import registration
from loginlogout.form import reg_Form
from django.contrib import messages

# user registration    
def store_reg(request):
	if request.method == "POST":
		model_form = reg_Form(request.POST)
		#model_form.save()
		if model_form.is_valid():
			model_form.save()
		else:
			model_form.save()
	else:
		model_form = reg_Form()
	return render(request, 'form.html', {'form': model_form})

#user login and logout   
def login(request):
	user_name_QS = request.POST.get("user_name")
	password_QS =  request.POST.get("password")
	if user_name_QS is None or password_QS is None:
		user_name_QS = "esther"
		password_QS = "esther23"
	else:
		mydict = registration.objects.get(user_name = user_name_QS)
		if mydict.password == password_QS:
			return render(request, "home.html")
		else:
			messages.error(request,'username or password not correct')	
			return("exit.html")
		
	return render(request,"login.html")	

	
def exit(request):
	  return render(request, 'exit.html', {})



   # else:
       # return render(request, 'login.html')

   # return  "0"
	              
	    
    

