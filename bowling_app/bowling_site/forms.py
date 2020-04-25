from django import forms
from .models import Bowler


# class BowlerForm(forms.ModelForm):
#     class Meta:
#         model = Bowler
#         fields = [
#             'first',
#             'middle',
#             'last',
#             'birthdate',
#             'gender',
#             'address',
#             'city',
#             'state',
#             'zipcode',
#             'email',
#             'username',
#             'password',
#         ]


class BowlerForm(forms.Form):
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
    avg = forms.IntegerField()
    hdcp = forms.IntegerField()


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
