from django.shortcuts import render
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
    orgs = models.EduOrg.orgs.all()
    context_dict['orgs'] = orgs
    return render(request, 'blog/edu.html', context_dict)


class TagIndex(generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = models.Tag.objects.get(slug=slug)
        results = models.Entry.posts.filter(tags=tag)
        return results
