from django.conf import settings
from .models import Author, Tag, Category, Post
from .forms import FeedbackForm
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.mail import mail_admins


def index(request):
    return HttpResponse("Hello Django")


# view function to display a list of posts
def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# view function to display a single post
def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)

# view function to display post by tag


def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/post_by_tag.html', context)


# view function to display post by author
def post_by_author(request, name):
    author = get_object_or_404(Author, name=name)
    posts = get_list_or_404(Post.objects.order_by("-id"), author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context)


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])

            try:
                mail_admins(subject, message)
                f.save()
                print("Success")
                message.add_message(request, message.SUCCESS, 'Feedback Sent!')
            except:
                print("Failed")
                message.add_message(request, message.INFO, 'Unable to send feedback, try again')

            return redirect('feedback')

    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})
