from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'post': posts}
    return render(request , 'post/post_page.html', context)