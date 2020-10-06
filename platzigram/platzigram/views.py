
#Django
from django.http import HttpResponse
import json

#utilities
from datetime import datetime

def hello_world(request): 
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now}'
    .format(now=now
    ))

def sorted(request): 
    """Sorted."""
    numbers=request.GET['numbers']
    list_numbers = list(numbers.split(','))#Divide los strings con comas y los almacena en una list
    list_numbers = list(map(int, list_numbers))#convierte la lista de los strings en enteros 
    list_numbers.sort()#ordena la lista
    return HttpResponse(
        json.dumps(list_numbers
        ))#regresara un json```

def say_hi(request, name, age):
    """return a greeting."""
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message= 'Hello {}! Welcome to platzigram'.format(name)
    return HttpResponse(message)
