from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Board, Topic, Post
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return HttpResponse('instantiated')

def boards_topics(request, board_id):
    '''
    try:
        board = Board.objects.get(pk=board_id)
        print(board)
    except Board.DoesNotExist:
        raise Http404
    '''
    board = get_object_or_404(Board, pk=board_id)    
    return render(request, 'topics.html', {'board': board})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        subject = request.POST['topic']
        textArea = request.POST['text']
        user = User.objects.first()
        topic = Topic.objects.create(
            subject = subject,
            board = board,
            creator = user,
        )
        post = Post.objects.create(
            message=textArea,
            topic = topic,
            creator=user
        )

        return HttpResponseRedirect('/boards/{<int: board_id/>}')
    return render(request, 'newTopic.html', {'board': board})