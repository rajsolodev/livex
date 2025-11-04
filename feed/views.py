from django.shortcuts import render, redirect
from django.core.cache import cache
from .forms import PostForm
from .models import Post

def feed_view(request):
  form = PostForm(request.POST or None)
  if request.method == "POST" and form.is_valid():
    post = form.save(commit=False)
    if request.user.is_authenticated:
      post.user = request.user
    else:
      post.user = None
    
    post.save()
    cache.delete('posts')
    return redirect('feed')
  
  posts = cache.get('posts')
  if not posts:
    posts = Post.objects.order_by('-created_at')[:20]
    cache.set('posts', posts, 5)
  return render(request, 'feed/index.html', {'form':form, 'posts':posts})


