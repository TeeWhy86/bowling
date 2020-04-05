from django.http import HttpResponse
from django.shortcuts import render
from .forms import RawCustomerForm, RawContactForm
from .models import Customer, Contact

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
    my_form = RawContactForm()
    if request.method == "POST":
        my_form = RawContactForm(request.POST)
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


def bowling_site_reg(request):
    my_form = RawCustomerForm()
    if request.method == "POST":
        my_form = RawCustomerForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Customer.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "bowling_site/customer_register.html", context)
