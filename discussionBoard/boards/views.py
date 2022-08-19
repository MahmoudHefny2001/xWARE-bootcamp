from django.http import HttpResponseRedirect, HttpResponse, Http404
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
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.post)
        if form.is_valid():
            topic = form.save(commit = False)
            topic.board = board
            topic.creator = user
            topic.save()
            
            post = post.objects.create(
                message = form.cleaned_data.get('message'),
                creator = user,
                topic = topic
            )
            return redirect('boards_topics', board_id = board.pk)
    else:
        form = NewTopicForm()       
    '''
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

        return redirect('boards_topics', board_id=board.pk)
        '''

    return render(request, 'newTopic.html', {'board': board, 'form': form})