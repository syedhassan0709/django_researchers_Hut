from django.shortcuts import render,HttpResponse , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm , UserPannelForm
#from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.urls import reverse
from .models import UserPannel
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib import messages

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
            authenticate_user = authenticate(username = new_user.email,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('users:createpannel'))
            
            
    context= {'form':form,}
    return render(request,'users/register2.html',context)
   
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('publications:home')) 

def login_view(request):
    logout(request)
    if request.method == 'POST':
        uname = request.POST.get('username') 
        passwor = request.POST.get('password')
        user = authenticate(username=uname,password=passwor)
        login(request,user)
        return HttpResponseRedirect(reverse('publications:home'))       

    return render(request,'users/login.html')

@login_required
def reserchers(request):
    resercher = UserPannel.objects.all()
    context = {'resercher':resercher}
    return render(request,'users/finalpannel.html',context)

    
@login_required  
def User_pannel_creation(request):
    '''Add a new topic'''
    # get from the browser
    if request.method != 'POST':
        # NO DATA SUBMITTED CREAT A BLANK FORM
        form = UserPannelForm()
    # post method    
    else:
        #POST DATA SUBMITED ; PROCESS DATA
        form = UserPannelForm(request.POST,request.FILES)
        if form.is_valid():
            
            user_pannel = form.save(commit=False)
            user_pannel.owner = request.user
           
            user_pannel.save()
            return HttpResponseRedirect(reverse('users:reserchers'))

    context = {'form' : form}
    return render(request,'users/User_pannel.html',context)         

@login_required
def myprofiles(request):
    myprofiles = UserPannel.objects.filter(owner=request.user)
    context = {'myprofiles':myprofiles}
    return render(request,'users/myprofiles.html',context)
@login_required
def delete(request, d_id):
    pannel = UserPannel.objects.get(id=d_id)
    if pannel.owner != request.user:
        raise Http404    
    
    if request.POST['yes'] == 'YES':
        pannel.delete()
        return HttpResponseRedirect(reverse('users:myprofiles'))
    context= {'r':pannel}    
    return render(request,'users/delete.html',context)



@login_required
def editprofile(request, p_id):
    pannel = UserPannel.objects.get(id=p_id)
    owner = pannel.owner
    if request.method != 'POST':
        form = UserPannelForm(instance=pannel)
    else:
        request.POST and request.FILES
        form = UserPannelForm(request.POST or None , request.FILES or None,instance=pannel)
        if form.is_valid():
            print(form.changed_data['name'])
            form.save()
            return HttpResponseRedirect(reverse('users:myprofiles'))    
        if pannel.owner != request.user:
            raise Http404
    #pannel = UserPannel.objects.get(id=p_id)
    #owner = pannel.owner
    #form = UserPannelForm(request.POST or None,request.FILES or None, instance=pannel)
    #if form.is_valid():
    #    form.save()
    #    return HttpResponseRedirect(reverse('users:myprofiles'))
    #if pannel.owner != request.user:
    #    raise Http404    
    context = {
        'form':form,
        'pannel':pannel,
        'owner':owner.username
    }
    return render(request, 'users/editpannel.html',context)       

def searchfunction(request):
    gender = request.GET['gender']
    field = request.GET['field']
    programme=request.GET['BS']
    college1 = request.GET['college']
    if gender == 'ANY':
        search_result_g_f = UserPannel.objects.filter(group=field)
    else:
        search_result_g_f = UserPannel.objects.filter(gender=gender).filter(group=field)
    if programme == '':
       final_result = search_result_g_f.filter(college__icontains=college1)
    if college1 == '':
       final_result = search_result_g_f.filter(programe__icontains=programme)
    if programme != '' and college1 != '':
        final_result = search_result_g_f.filter(programe__icontains=programme).filter(college__icontains=college1)   

    print(gender,field,programme,college1 )
    context = {'result': final_result}
    return render(request,'users/search.html',context)