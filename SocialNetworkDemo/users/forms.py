from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User


class UserSignInForm(AuthenticationForm):
    username = UsernameField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        )
    )


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class UsersSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Фамилия, имя или никнейм'
    )
