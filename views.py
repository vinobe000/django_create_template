#view.py file in app folder
from django.shortcuts import render
def index(request):
    return render(request,"index.html",{})

