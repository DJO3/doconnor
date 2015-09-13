from django.contrib.syndication.views import Feed
from blog.models import Entry


class LatestPosts(Feed):
    title = 'doconnor blog'
    link = "/feed/"
    description = 'Exploring Python, Django and everything in between.'

    def items(self):
        return Entry.posts.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        words = item.body[:600].split()[:58]
        description = ' '.join(words)
        return description