from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import BowlerForm, BowlerForm2, ContactForm
from .models import Bowler, Contact


# Create your views here.


def index(request):
    return HttpResponse('This is the Index Page...')


def bowling_site_home(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "BowlersBliss.html")


def bowling_site_bowler(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "Bowlers.html")


def bowling_site_about(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "About.html")


# def bowling_site_reg(request):
#
#     # render function takes argument - request
#     # and return HTML as response
#     return render(request, "BowlersBlissRegistration.html")


# def bowling_site_contact(request):
#     my_form = ContactForm()
#     if request.method == "POST":
#         my_form = ContactForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Contact.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "bowling_site/Contact.html", context)
def bowling_site_contact(request):
    form = ContactForm()
    if form.is_valid():
        form.save()
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "bowling_site/Contact.html", context)


def bowling_site_log(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "Login.html")


def bowling_site_wip(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "WIP.html")


# def create_bowler(request):
#     form = BowlerForm()
#     form2 = BowlerForm2()
#     if request.method == "POST":
#         form = BowlerForm(request.POST)
#         form2 = BowlerForm2(request.POST)
#         if form.is_valid() & form2.is_valid():
#             print(form.cleaned_data)
#             Bowler.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#             print(form2.errors)
#     context = {
#         'form': form,
#         'form2': form2,
#     }
#     return render(request, "bowling_site/bowler_form.html", context)


def create_bowler(request):
    form = BowlerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BowlerForm()

    context = {
        'form': form
    }

    # context[form] = form
    return render(request, "bowling_site/bowler_form.html", context)


def edit_bowler(request, id):
    context = {}
    obj = get_object_or_404(Bowler, id=id)
    form = BowlerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form
    return render(request, "bowling_site/bowler_edit.html", context)


def list_bowler(request):
    context = {}
    context["dataset"] = Bowler.objects.all()
    return render(request, "bowling_site/bowler_list.html", context)


def delete_bowler(request, id):
    context = {}
    obj = get_object_or_404(Bowler, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "bowling_site/bowler_delete.html", context)
