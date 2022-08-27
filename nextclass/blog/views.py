from multiprocessing import context
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

posts = [
    {
        "title" : "Les gens sont dans la rue",
        "author" : "Landry Serigba",
        "content" : "Nous avons appris ça hier, le monde est perdu. Beaucoup sont dans les choses bizarres.",
        "date" : "28 septembre 2022"
    },

    {
        "title" : "Abidjan ville lumière",
        "author" : "Serge Didier",
        "content" : "L'idée était de prendre tous les hommes et de les manger.Nous avons appris ça hier, le monde est perdu. Beaucoup sont dans les choses bizarres.",
        "date" : "14 septembre 2022"
    }
]

def home(request):
    context ={
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
