from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import Create_task_form
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.

def default_view(request):
    return HttpResponse("Hello World")



def create_task(request):
    
    if request.method == 'GET':
        return render(request,'todo/createTask.html')
    else:
        form = Create_task_form(request.POST)
        task = Task(
            name = form.cleaned_data['username'],
        )
        task.save()
            


def retrieve_task(request):
    task = task.objects.get(id=request.GET['id'])
    return render(request, 'todo/retrieveTask.html')


def list_tasks(request):

    tasks = Task.objects.all()

    tasksList = []

    '''
    for task in tasks:
        tasksList.append({
            'name': task.name,
        })
    return render(request, 'todo/listTasks.html', {'tasks': tasks})
    '''

def update_task(request):
    return render(request, 'todo/updateTask.html')
def delete_task(request):
    return render(request, 'todo/deleteTask.html')
