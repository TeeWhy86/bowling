from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class BowlerForm(forms.ModelForm):
    class Meta:
        model = Bowler
        fields = [
            'first',
            'middle',
            'last',
            'Birth Date',
            'gender',
            'address',
            'city',
            'state',
            'zipcode',
            'email',
            'username',
            'password',
        ]


# class BowlerForm(forms.Form):
#     first = forms.CharField(
#         label='First',
#     )
#     middle = forms.CharField(
#         label='Middle',
#         required=False
#     )
#     last = forms.CharField(
#         label='Last',
#     )
#     birthdate = forms.DateField(
#         label='Birth Date',
#     )
#     gender = forms.ChoiceField(
#         label="Gender",
#         choices=((1, "Female"), (2, "Male")),
#         # required=False,
#         widget=forms.RadioSelect,
#         initial='1'
#     )
#     address = forms.CharField(
#         required=False
#     )
#     city = forms.CharField(
#         required=False
#     )
#     state = forms.CharField(
#         required=False
#     )
#     zipcode = forms.IntegerField(
#         required=False
#     )


class BowlerForm2(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    avg = forms.IntegerField()
    hdcp = forms.IntegerField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message',
        ]
