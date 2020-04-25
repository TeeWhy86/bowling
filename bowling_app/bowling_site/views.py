from django.http import HttpResponse
from django.shortcuts import render
from .forms import BowlerForm, ContactForm
from .models import Bowler, Contact

# Create your views here.


def index(request):
    return HttpResponse('This is the Index Page...')


def bowling_site_home(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "BowlersBliss.html")


def bowling_site_about(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "About.html")


# def bowling_site_reg(request):
#
#     # render function takes argument - request
#     # and return HTML as response
#     return render(request, "BowlersBlissRegistration.html")


def bowling_site_contact(request):
    my_form = ContactForm()
    if request.method == "POST":
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Contact.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "bowling_site/contact_form.html", context)


def bowling_site_log(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "Login.html")


def bowling_site_wip(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "WIP.html")


def create_bowler(request):
    form = BowlerForm()
    form1 = ContactForm()
    if request.method == "POST":
        form = BowlerForm(request.POST)
        form1 = ContactForm(request.POST)
        if form.is_valid() & form1.is_valid():
            print(form.cleaned_data)
            print(form1.cleaned_data)
            Bowler.objects.create(**form.cleaned_data)
            Contact.objects.create(**form1.cleaned_data)
        else:
            print(form.errors)
            print(form1.errors)
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, "bowling_site/bowler_form.html", context)
