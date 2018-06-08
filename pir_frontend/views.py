from django.shortcuts import render
from django import forms


# Create your views here.
def form_base(request):
    return render(request, 'index.html')
