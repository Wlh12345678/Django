from django.contrib.syndication.views import Feed
from .models import Post
from django.shortcuts import reverse
class PostFeed(Feed):
    """
    进行网站包装
    """
    title = '文章'
    description = '摘要'
    link = '/'
    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.ptitle

    def item_description(self, item):
        return item.psummary

    def item_link(self, item):
        return reverse('blogtest:detail',args=(item.id,))


