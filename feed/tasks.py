from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.cache import cache
from feed.models import Post
import random

@shared_task
def rotate_trending_post():
  posts = cache.get('posts')
  if not posts:
    posts = list(Post.objects.order_by('-created_at')[:20])
    if not posts:
        print("No posts found in database, skipping trending rotation")
        return
  
  # Convert to list if needed
  if hasattr(posts, '__iter__') and not isinstance(posts, list):
      posts = list(posts)

  # Pick 3 random posts (or you can pick top 3 by likes/comments if you have metrics)
  trending_posts = random.sample(posts, min(len(posts), 3))

  channel_layer = get_channel_layer()
  for idx, post in enumerate(trending_posts, start=1):
     async_to_sync(channel_layer.group_send)('feed', {
        "type": "new_post",
        "content": post.content,
        "username": post.display_user,
        "post_type": "trending",
        "rank": idx
     })
