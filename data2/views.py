from django.shortcuts import render
from django.views.generic import ListView
from .models import B

# Create your views here.


class B(ListView):
    model = B
    template_name = 'index2.html'