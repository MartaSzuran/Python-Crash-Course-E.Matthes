from django.shortcuts import render
from blogs.models import BlogPost

from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import BlogPostForm


# Create your views here.
def main(request):
    """Main site to application blogs."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/main.html', context)


@login_required
def new_post(request):
    """Add new post."""
    if request.method != 'POST':
        # no pass data create new form
        form = BlogPostForm()

    else:
        # data passed with POST, need to process them
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            form.save()
            return HttpResponseRedirect(reverse('main'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit already created post."""
    post = BlogPost.objects.get(id=post_id)
    blog_text = post.text

    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))

    context = {'text': blog_text, 'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
