from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserPannel
# phone number
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



# USER MODEL
from django.contrib.auth import get_user_model
User = get_user_model()
#

class CreatUserForm(UserCreationForm):



    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'name':"username",
            'id':"username",
            'placeholder':"Enter your Username with out SPACES",
        })
        self.fields['email'].widget.attrs.update({
            ' type':"text",
            'class':"form-control",
            'name':"email",
            'id':"email",
            ' placeholder':"Enter your Email",
        })
        self.fields['password1'].widget.attrs.update({
            ' type':"password",
            'class':"form-control",
            'name':"password",
            'id':"password",
            ' placeholder':"Enter your Password",
        })
        self.fields['password2'].widget.attrs.update({
            ' type':"password",
            'class':"form-control",
            'name':"confirm",
            'id':"confirm",
            ' placeholder':"Confirm your Password",
        })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        ''' widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }'''  

class UserPannelForm(forms.ModelForm): 
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='PK')

    )

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class':"form-control",
            'placeholder':"Enter Your Name"
        })
        self.fields['gender'].widget.attrs.update({
            'class':"form-control",
        })
        self.fields['phone'].widget.attrs.update({
            'class':"form-control",
            'placeholder':"Enter Your Phone Number default = 03000000000"
        })    
        self.fields['group'].widget.attrs.update({
            'class':"form-control",
        })
        self.fields['college'].widget.attrs.update({
            'class':"form-control",
            'placeholder':'Name of INSTITUTION'
        })
        self.fields['programe'].widget.attrs.update({
            'class':"form-control",
            'placeholder':"BS Programe"
        })
        self.fields['level'].widget.attrs.update({
            'class':"form-control",
            'placeholder':"Year"
        })
        self.fields['topic'].widget.attrs.update({
            'class':"form-control",
            'placeholder':"Research Topic"
        })
        self.fields['profile_pic'].widget.attrs.update({
            'class':"form-control",
        })
        self.fields['description'].widget.attrs.update({
            'class':"form-control",
        })    
    class Meta:
        model = UserPannel
        fields = ['name','gender','phone','group','college','programe','level','topic','profile_pic','description']
        wedgets = {'description':forms.Textarea(attrs={'cols' : 30})}