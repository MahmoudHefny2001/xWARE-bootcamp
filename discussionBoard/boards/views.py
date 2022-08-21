from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms import NewTopicForm
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return HttpResponse('instantiated')

def boards_topics(request, board_id):
    
    board = get_object_or_404(Board, pk=board_id)    
    return render(request, 'topics.html', {'board': board})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit = False)
            topic.board = board
            topic.creator = user
            topic.save()
            
            post = Post.objects.create(
                essay = form.cleaned_data.get('essay'),
                creator = user,
                topic = topic
            )
            return redirect('boards_topics', board_id = board.pk)
    else:
        form = NewTopicForm()       
   
    return render(request, 'newTopic.html', {'board': board, 'form': form})

