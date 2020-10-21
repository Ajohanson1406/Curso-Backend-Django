"""posts views."""

#Django
from django.shortcuts import render
#Utilities
from datetime import datetime


posts = [
    {
        'title': 'Blackie',
        'user': {
            'name': 'Barbara Johanson',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timesstamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200',
    },
    {
        'title': 'Shu Swamp',
         'user': {
            'name': 'Christian van der henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timesstamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200',
    },
    {
        'title': 'Rainy Day',
         'user': {
            'name': 'Albert Johanson',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timesstamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200',
    }
]


# Create your views here.

def list_posts(request):
    """list existing posts."""

    return render(request, 'posts/feed.html', {'posts': posts})
   