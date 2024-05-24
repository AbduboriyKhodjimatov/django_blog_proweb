from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ваш комментарий'
            })
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'

    }))

    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'

    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'

    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'}),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            })

        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'short_description', 'full_description', 'preview', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'

            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ' Краткое описание'

            }),
            'full_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ' Полное описание'

            }),
            'preview': forms.FileInput(attrs={
                'class': 'form-control'

            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })

        }



