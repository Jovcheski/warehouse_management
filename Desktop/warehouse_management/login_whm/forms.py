from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={'class': 'input'}),
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
        }


