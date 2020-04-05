from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first',
            'middle',
            'last',
            'birthdate',
            'gender',
            'email',
            'username',
            'password',
        ]


class RawCustomerForm(forms.Form):
    first = forms.CharField()
    middle = forms.CharField(required=False)
    last = forms.CharField()
    birthdate = forms.DateField()
    gender = forms.CharField(required=False)
    address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    zipcode = forms.IntegerField(required=False)
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RawContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
