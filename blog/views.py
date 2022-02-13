from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')
def academic(request):
    return render(request, 'blog/academic.html')
def contact(request):
    return render(request, 'blog/contact.html')