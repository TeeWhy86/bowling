# from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', index),
    path('home', bowling_site_home),
    path('bowlers', bowling_site_bowler),
    path('about', bowling_site_about),
    path('reg', create_bowler),
    path('list', list_bowler),
    path('edit/<id>', edit_bowler),
    path('delete/<id>', delete_bowler),
    path('contact', bowling_site_contact),
    path('log', bowling_site_log),
    path('wip', bowling_site_wip),
]
