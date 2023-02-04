from django.contrib.syndication.views import Feed
from django.urls import reverse
from Blog_App.models import Post

class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/rss/feed"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
