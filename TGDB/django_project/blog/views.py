from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import Author, Tag, Category, Post
from django.shortcuts import redirect, Http404, get_object_or_404, get_list_or_404


def index(request):
    return HttpResponse("Hello Django")

# view function to display a list of posts

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# view function to display a single post

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category

def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)

# view function to display post by tag

def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context)


# view function to display post by author
def post_by_author(request, name):
    author = get_object_or_404(Author, name=name)
    posts = get_list_or_404(Post, author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context )
