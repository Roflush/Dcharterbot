from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def history(request):
    return render(request, "history.html")

def commands(request):
    return render(request, "commands.html")

def db(request):

  # greeting = Greeting()
  #  greeting.save()

 #   greetings = Greeting.objects.all()

   # return render(request, "db.html", {"greetings": greetings})
   return request(request, "sup")
