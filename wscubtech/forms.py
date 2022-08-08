from logging import PlaceHolder
from django import forms


class userForm(forms.Form):
    num1 = forms.CharField(label='Data1',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    num2 = forms.CharField(label='Data2',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    num3 = forms.CharField(label='Data3',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

  