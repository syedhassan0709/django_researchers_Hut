from django.shortcuts import render,HttpResponse , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.urls import reverse
from .models import UserPannel
# Create your views here.
def registerationPage(request):
    #if request.method == "POST":
    #    uname = request.POST.get('username')                               help   
    #    email = request.POST.get('email')                                  help   
    #    pass1 = request.POST.get('password')                               help
    #    pass2 = request.POST.get('confirm')                                help    
    #    my_user = User.objects.create_user(uname,email,pass1)              help
    #    my_user.save()
    #    return HttpResponse('Usr has been created'  
    if request.method != 'POST':
        form = CreatUserForm()
    else:
        form = CreatUserForm(request.POST)    
        if form.is_valid:
            new_user = form.save()
            authenticate_user = authenticate(username = new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('publications:home'))
    context= {'form':form}
    return render(request,'users/register2.html',context)
   
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('publications:home')) 

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username') 
        passwor = request.POST.get('password')
        user = authenticate(username=uname,password=passwor)
        login(request,user)
        return HttpResponseRedirect(reverse('publications:home'))        

    return render(request,'users/login.html')


def reserchers(request):
    time = User.last_login
    resercher = UserPannel.objects.all().order_by('owner')
    context = {'resercher':resercher}
    print(time)
    return time

reserchers()