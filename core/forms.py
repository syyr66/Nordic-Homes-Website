from django import forms 
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50, label="First name", required=True, 
        widget=forms.TextInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    last_name = forms.CharField(
        max_length=50, label="Last name", required=True, 
        widget=forms.TextInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    username = forms.CharField(
        max_length=50, label="Username", required=True, 
        widget=forms.TextInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    email = forms.EmailField(
        max_length=255, label="Email", required=True, 
        widget=forms.TextInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    password1 = forms.CharField(
        max_length=255, label="Password", required=True, 
        widget=forms.PasswordInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    password2 = forms.CharField(
        max_length=255, label="Repeat password", required=True, 
        widget=forms.PasswordInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")


class LogInForm(forms.Form):
    username = forms.CharField(
        max_length=50, label="Username", required=True, 
        widget=forms.TextInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )
    password = forms.CharField(
        max_length=255, label="Password", required=True, 
        widget=forms.PasswordInput(attrs={"class":"w-full mt-2 py-4 px-6 bg-white rounded-xl"})
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cd = self.cleaned_data
        username = cd.get('username')
        passwd = cd.get('password')

        user = authenticate(self.request, username=username, password=passwd)
        if user == None:
            raise ValidationError("invalid username or password")
        
        self.user = user

    def get_user(self):
        return self.user

class AccountForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First name',
            'last_name': 'Last name',
        }


class EditAccountForm(AccountForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['first_name'].widget.attrs['placeholder'] = self.instance.first_name or 'Enter your first name'
            self.fields['email'].widget.attrs['placeholder'] = self.instance.email or 'Enter your email'
            self.fields['last_name'].widget.attrs['placeholder'] = self.instance.last_name or 'Enter your last name'


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'}),
            'email': forms.TextInput(attrs={'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'}),
            'first_name': forms.TextInput(attrs={'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'}),
        }


# class EditAccountForm(forms.ModelForm):
#     username = forms.CharField(
#         max_length=50,
#         label="Username",
#         disabled=True,
#         widget=forms.TextInput(attrs={
#             'class': 'inline-block w-80 mt-2 py-2 px-4 text-purple-800 bg-white border border-purple-500 rounded-md'
#         })
#     )

#     email = forms.EmailField(
#         max_length=255,
#         label="Email",
#         disabled=True,
#         widget=forms.TextInput(attrs={
#             'class': 'inline-block w-80 mt-2 py-2 px-4 text-purple-800 bg-white border border-purple-500 rounded-md'
#         })
#     )

#     first_name = forms.CharField(
#         max_length=50,
#         label="First name",
#         widget=forms.TextInput(attrs={
#             'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'
#         })
#     )

#     last_name = forms.CharField(
#         max_length=50,
#         label="Last name",
#         widget=forms.TextInput(attrs={
#             'class': 'inline-block w-80 mt-2 py-2 px-4 bg-white border border-gray-300 rounded-md'
#         })
#     )

#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name', 'last_name']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance:
#             self.fields['first_name'].widget.attrs['placeholder'] = self.instance.first_name or 'Enter your first name'
#             self.fields['last_name'].widget.attrs['placeholder'] = self.instance.last_name or 'Enter your last name'
