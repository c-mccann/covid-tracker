from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('covid', views.covid),
    path('info', views.downloadinfo, name="downloadinfo"),

    # redirect
    # path('', lambda request: redirect('covid', permanent=False)),
]