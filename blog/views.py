from django.shortcuts import render, HttpResponse
from django.views import generic
from blog import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.posts.published()
    template_name = 'blog/index.html'
    paginate_by = 5


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'blog/post.html'


def about(request):
    context_dict = {}
    return render(request, 'blog/about.html', context_dict)


def edu(request):
    context_dict = {}
    return render(request, 'blog/edu.html', context_dict)
