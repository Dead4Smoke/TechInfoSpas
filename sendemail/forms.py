
from django.forms import ModelForm, TextInput, EmailInput

from django import forms

class RegForm(forms.Form):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    secondname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.CharField(label='Возраст', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    address = forms.CharField(label='Адрес проживания', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    team = forms.CharField(label='Команда', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    role = forms.CharField(label='Роль в команде', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    data = forms.CharField(label='Я согласен на обработку персональных данных', widget=forms.CheckboxInput(attrs={'class':'form-control1'}), required=True)
    hack = forms.CharField(label='Я ознакомлен с положением о проведении конкурса', widget=forms.CheckboxInput(attrs={'class':'form-control1'}), required=True)
