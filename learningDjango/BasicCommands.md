- activate the virtual environment
# source env/bin/activate

- installing django
# pip3 install django==3.2

- check Django version
# python3 -m django --version

- run the server
# python3 manage.py runserver

- create your project 
# django-admin startproject <project name>

- running project server as local host
# python3 manage.py runserver

-  link to the website
# http://127.0.0.1:8000/

- changing the port number
# python3 manage.py runserver <port number>

- changing the server IP
# python3 manage.py runserver 0:8000

- Creating the Polls app
# python3 manage.py startapp polls

- Leaving port
# sudo fuser -k 8000/tcp

## Write your first view
	
	- cd polls
	- vim views.py
	
	 - from django.http import HttpResponse
		- def index(request):
    		- return HttpResponse("Hello, world. You're at the polls index.")





