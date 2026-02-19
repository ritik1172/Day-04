from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to myDict',
        'created_at': datetime.now(),
        'Price': 100,
        'is_published': False,
        'tags': ['Python', 'Html', 'Django'],
    }
    return render(request, 'home.html', context)

def about(request):
    blog = [ {'title': 'Blog 1', 'content': 'Blog 1 content', 'isPublished': True},
              {'title': 'Blog 2', 'content': 'Blog 2 content', 'isPublished': True},
             ]
    
    context = {
        'blog': blog,
        'content': 'This is about page',
        'created_at': datetime.now(),
    }
    return render(request, 'about.html', context)
    