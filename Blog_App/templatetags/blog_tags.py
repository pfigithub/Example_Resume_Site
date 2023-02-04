from django import template
from Blog_App.models import Post, Comment
from Blog_App.models import Category

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg = 4):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories':cat_dict}


@register.simple_tag(name='comments_count')
def commentcount(pid):
    return Comment.objects.filter(post= pid, approved=True).count()
    context = {'post': post, 'comments':comments}