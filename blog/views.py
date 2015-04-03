from django.shortcuts import render


def index(request):
    context_dict = {}
    return render(request, 'blog/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'blog/about.html', context_dict)