from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from  django.db.models import Q
# Create your views here.

def post_index(request):
    post_list = Post.objects.all()
    query=request.GET.get("q")
    if  query:
        post_list=post_list.filter(Q(title__icontains=query)|
                                   Q(user__first_name__icontains=query)|
                                   Q(body__icontains=query))
    paginator = Paginator(post_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Comment created succesfully")
            return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form':form,
    }
    return render(request, "post/detail.html", context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted succesfully")
    return redirect("post:index")


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created succesfully")
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()
    Post.objects.create
    context = {
        'form': form
    }
    return render(request, "post/form.html", context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST":

        if form.is_valid():
            post = form.save()
            messages.success(request, "Post updated succesfully")
            return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "post/form.html", context)
