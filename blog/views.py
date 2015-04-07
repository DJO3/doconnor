from django.shortcuts import render, HttpResponse
from django.views import generic
from blog import models
from twitter_feed.models import Tweet


class BlogIndex(generic.ListView):
    queryset = models.Entry.posts.published()
    template_name = 'blog/index.html'
    paginate_by = 5


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = 'blog/post.html'


def about(request):
    context_dict = {'tweets': Tweet.objects.all()[:5]}
    return render(request, 'blog/about.html', context_dict)
