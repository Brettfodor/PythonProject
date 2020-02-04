import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "hello/home.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def about(request):
    return render(request, "hello/about.html")
    
print("http://127.0.0.1:8000/hello/VSCode")


