from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django import http
from .forms import Create_user_form
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def default_view(request):
    return HttpResponse("<p>Create user</p>")



def delete_user(request):
    try:
        user = User.objects.get(id=request.GET['id'])
        user.delete()
        return render(request, 'user/deleteUser.html', {
            'result': 'User deleted'
        })
    except Exception:
        return render(request, 'user/deleteUser.html', {
            'result': 'User Not Found'
        })


@require_http_methods('GET')
def list_users(request):
    first_time = True
    if 'first_time' in request.COOKIES:
        first_time = False
    users = User.objects.all()
    user_list = []
    for user in users :
        user_name = user.name
        user_email = user.email
        user_age = user.password
        user_list.append({
            'first_time': first_time,
            'user_name' : user_name,
            'user_email': user_email,
            'user_age' : user_age,
        })
    print(first_time)
    response =  render(request, 'user/listUsers.html', {
        'first_time': first_time,
        'users_list': user_list
    })
    response.set_cookie('first_time', 'True')
    return response

def retreive_user(request):
    try:
        user = User.objects.get(id=request.GET['id'])
        return render(request, 'user/retrieveUser.html',{
            'is_user_found': True,
            'user': user
        })
    except:
        return render(request, 'user/retrieveUser.html',{
            'is_user_found': False
        })








class CreateUserView(View):

    def get(self, request):
        if request.method == 'GET':
            return render(request,'user/createUser.html')
        else:
            form = Create_user_form(request.POST)
            if form.is_valid():
                user = User(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['Email'],
                    password = form.cleaned_data['password']
                )
                user.save()
                return render(request, 'user/createUser.html', {
                    'result': 'Valid',
                    'validated_user_name' : user.username,
                    'validated_user_email': user.Email,
                    'validated_password' : user.password,
                    'user' : user
                })
            else :
                return render(request, 'user/createUser.html', {
                    'result' : 'Not Valied' ,
                })
    def post(self, request):
        if request.method == 'GET':
            return render(request,'user/createUser.html')
        else:
            form = Create_user_form(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['Email'],
                    password = form.cleaned_data['password']
                )
                user.save()
                return render(request, 'user/createUser.html', {
                    'result': 'Valid',
                    'validated_user_name' : user.username,
                    'validated_user_email': user.email,
                    'validated_password' : user.password,
                    'user' : user
                })
            else :
                return render(request, 'user/createUser.html', {
                    'result' : 'Not Valied' ,
                })








class loginView():
    def get(self, request):
        if request.method == 'POST' :
            request.session['username'] = request.POST['username']
            request.session['password'] = request.POST['password']
            return render(request, 'user/login.html')
                
    def post(self, request):
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return render(request, 'user/login.html', {
                'logged' : True
            })
        print(user)
        return render(request, 'user/login.html', {
            'error': 'Username Or password is Wrong'
        })