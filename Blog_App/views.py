from django.shortcuts import render, get_object_or_404
from Blog_App.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Blog_App.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def blog_view(req, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name= kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username= kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    
    posts = Paginator(posts,2)
    
    try:
        page_number = req.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)


def blog_single(req, pid):
    counted = Post.objects.get(id=pid)
    counted.counted_views = counted.counted_views + 1
    counted.save()
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req, messages.SUCCESS, 'your comment submitted successfully')
        else:
            messages.add_message(req, messages.ERROR, 'your comment did not submitted')

    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid, status =1)
    if not post.login_require:
        comments = Comment.objects.filter(post= post.id, approved=True)
        form = CommentForm()
        context = {'post': post, 'comments':comments, 'form':form}
        return render(req, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('account_login'))


def blog_category(req, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)


def blog_search(req):
    posts = Post.objects.filter(status=1)
    if req.method == 'GET':
        if s:= req.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)