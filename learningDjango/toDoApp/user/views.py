from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User
from .forms import Create_user_form

def default_view(request):
    return HttpResponse("<p>Create user</p>")






def list_users(request):
    
    users = User.objects.all()

    users_list = []

    for user in users:
        users_list.append({
            'username': user.name,
            'Email': user.email,
            'password': user.password
        })
    return render(request, 'user/listUsers.html', {'users': users_list})



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






def create_user(request):

    if request.method == 'GET':
        return render(request,'user/todo_create.html')
    else:
        form = Create_user_form(request.POST)
        if form.is_valid():
            user = User(
                name = form.cleaned_data['username'],
                email = form.cleaned_data['Email'],
                password = form.cleaned_data['password'],
            )
            user.save()
            return render(request, 'user/todo_create.html', {
                'result': 'Valid',
                'validated_user_name' : user.name,
                'validated_user_email': user.email,
            })
        else :
            return render(request, 'user/todo_create.html', {
                'result' : 'Not Valied' ,
            })


