from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Comment, Profile


# Home Page with Search + Pagination
def home(request):

    query = request.GET.get('q')

    if query:

        posts = Post.objects.filter(
            title__icontains=query
        ).order_by('-id')

    else:

        posts = Post.objects.all().order_by('-id')

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'posts': page_obj,
        'query': query,
        'page_obj': page_obj
    })


# Register Page
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            # Create Profile Automatically
            Profile.objects.create(user=user)

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form
    })


# Create Post
@login_required
def create_post(request):

    if request.method == 'POST':

        title = request.POST['title']

        content = request.POST['content']

        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            image=image
        )

        return redirect('home')

    return render(request, 'create_post.html')


# Edit Post
@login_required
def edit_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':

        post.title = request.POST['title']

        post.content = request.POST['content']

        if request.FILES.get('image'):

            post.image = request.FILES.get('image')

        post.save()

        return redirect('home')

    return render(request, 'edit_post.html', {
        'post': post
    })


# Delete Post
@login_required
def delete_post(request, id):

    post = get_object_or_404(Post, id=id)

    post.delete()

    return redirect('home')


# Add Comment
@login_required
def add_comment(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':

        text = request.POST.get('text')

        if text:

            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    return redirect('home')


# Like Post
@login_required
def like_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.user in post.likes.all():

        post.likes.remove(request.user)

    else:

        post.likes.add(request.user)

    return redirect('home')


# Profile Page
@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    # User Posts
    user_posts = Post.objects.filter().order_by('-id')

    # Stats
    total_posts = user_posts.count()

    total_likes = Post.objects.filter(
        likes=request.user
    ).count()

    total_comments = Comment.objects.filter(
        user=request.user
    ).count()

    return render(request, 'profile.html', {

        'profile': profile,

        'user_posts': user_posts,

        'total_posts': total_posts,

        'total_likes': total_likes,

        'total_comments': total_comments

    })


# Edit Profile
@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        profile.bio = request.POST.get('bio')

        if request.FILES.get('profile_image'):

            profile.profile_image = request.FILES.get(
                'profile_image'
            )

        profile.save()

        return redirect('profile')

    return render(request, 'edit_profile.html', {

        'profile': profile

    })