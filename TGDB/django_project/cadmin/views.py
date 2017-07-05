from blog.forms import PostForm
from blog.models import Post, Author, Category, Tag
from django.shortcuts import render, redirect, get_object_or_404, reverse

# Create your views here.


def post_add(request):

    # If request is POST, create a bound form (form with data)
    if request.method == "POST":
        f = PostForm(request.POST)

        # check whether form is valid or not
        # if the form is valid, save the data to the database
        # and redirect the user back to the add post form

        # If form is invalid show form with errors again
        if f.is_valid():
            #  save data
            f.save()
            return redirect('post_add')

    # if request is GET the show unbound form to the user
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.html', {'form': f})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # If request is POST, create a bound form(form with data)
    if request.method == "POST":
        f = PostForm(request.POST, instance=post)

        # check whether form is valid or not
        # if the form is valid, save the data to the database
        # and redirect the user back to the update post form

        # If form is invalid show form with errors again
        if f.is_valid():
            f.save()
            return redirect(reverse('post_update', args=[post.id]))

    # if request is GET the show unbound form to the user, along with data
    else:
        f = PostForm(instance=post)

    return render(request, 'cadmin/post_update.html', {'form': f, 'post': post})
