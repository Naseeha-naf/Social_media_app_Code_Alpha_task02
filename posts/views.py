from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm


@login_required
def feed_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("feed")

    posts = Post.objects.all().order_by("-created_at")

    # add "is_liked" property for each post
    for post in posts:
        post.is_liked = Like.objects.filter(post=post, user=request.user).exists()

    return render(request, "posts/feed.html", {"form": form, "posts": posts})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        # already liked → unlike
        like.delete()
    return redirect("feed")


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(post=post, user=request.user, text=text)
    return redirect("feed")
