# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from first_choice.models import Video, Image
from django.views.generic.list import ListView

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/contact.html', {'content':['This is a testing contact, please email','zowski@hotmail']})

def about_us(request):
    return render(request, 'personal/about_us.html')

def portfolio(request):
    return render(request, 'personal/portfolio.html')


class ImagesListView(ListView):
    model = Image


# Create your views here.
