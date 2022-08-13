
from django.contrib import admin
from django.urls import path
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name=""),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
]
