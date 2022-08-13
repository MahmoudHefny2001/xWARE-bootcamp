from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def basic_view(request):
    return HttpResponse("")

def home_view(request, *args, **kwargs):       # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, 'home.html', {})

def login_view(request):
    return render(request, 'login.html', {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": str("+201065717371"),
        "my_list": [1, 2, 3]
    }
    
    return render(request, 'about.html', my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")