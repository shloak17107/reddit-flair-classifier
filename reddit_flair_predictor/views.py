from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 17, 2018'
    },
    {
        'author': 'oisjeofes',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 13, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'reddit_flair_predictor/home.html', context)
