from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from user import views
from todo import views as VIEWS
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', user.default_view),
    path('user/create/', views.CreateUserView.as_view()),
    path('user/list/' , views.list_users),
    path('user/retrieve/', views.retreive_user),
    path('user/delete/', views.delete_user),
    path('todo/', VIEWS.default_view),
    path('todo/create', VIEWS.create_task),
    path('todo/delete', VIEWS.delete_task),
    path('todo/retrieve', VIEWS.retrieve_task),
    path('todo/update', VIEWS.update_task),
    path('todo/list', VIEWS.list_tasks),
    path('login/', views.login),
    path('logout/', views.logout)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

