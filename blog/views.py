from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.
def post_list(request):
    publicaciones = Post.objects.filter (published_date__lte = timezone.now())
    return render(request, 'blog/post_list.html', {'publicaciones': publicaciones})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'publicacion': post})