"demo file"
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    
    return render(request, 'index.html ')
    #return HttpResponse('''<h1>The Sky </h1> <a href='https://www.youtube.com/channel/UCYgNPd-_cCaBwcymBQ7sW8w'> MEWTON GAMING </a>''')

def about (request):
    return HttpResponse("About Akash")
def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")