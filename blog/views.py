from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Favorite, CustomUser
from .forms import PostForm, CommentForm, CustomUserCreationForm, ProfilePictureForm, PostPictureForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

##########POSTS###############

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, post=post).exists()
    
    favorite_text = 'Unfavorite' if is_favorited else 'Favorite'
    button_class = 'btn-danger' if is_favorited else 'btn-primary'
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'is_favorited': is_favorited,
        'favorite_text': favorite_text,
        'button_class': button_class,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            if post.image:
                print("Image URL:", post.image.url)  # Depuración
            else:
                print("No image uploaded.")
            
            return redirect('post_detail', pk=post.pk)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})



########FAVORITES############

@login_required
def toggle_favorite(request, pk):
    post = get_object_or_404(Post, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
    if not created:
        favorite.delete()
    return redirect('post_detail', pk=post.pk)

@login_required
def favorite_list(request):
    user = request.user
    favorite_posts = user.favorite_posts.all()
    return render(request, 'blog/favorite_list.html', {'favorite_posts': favorite_posts})


#######COMMENTS####################

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

def load_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'blog/comments_list.html', {'comments': comments})

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def private_area(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/private_area.html', {'posts': posts})

##########PICTURES#############

@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('private_area')
    else:
        form = ProfilePictureForm(instance=request.user)
    return render(request, 'blog/upload_profile_picture.html', {'form': form})

@login_required
def upload_post_picture(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostPictureForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            print("Image URL after save:", post.image.url)  # Depuración
            return redirect('post_detail', pk=post.pk)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = PostPictureForm(instance=post)
    return render(request, 'blog/upload_post_picture.html', {'form': form, 'post': post})

