from Blog_App.views import *
from django.urls import path
from Blog_App.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index_blog'),
    path('category/<str:cat_name>', blog_view, name = 'category'),
    path('tag/<str:tag_name>', blog_view, name = 'tag'),
    path('author/<str:author_username>', blog_view, name = 'author'),
    path('search/', blog_search, name= 'search'),
    path('<int:pid>', blog_single, name = 'single_blog'),
    path('rss/feed/', LatestEntriesFeed())
]