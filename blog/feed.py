from django.contrib.syndication.views import Feed
from blog.models import Entry


class LatestPosts(Feed):
    title = 'doconnor blog'
    link = "/feed/"
    description = 'recent posts'

    def items(self):
        return Entry.posts.published()[:5]