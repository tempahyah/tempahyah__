from django.shortcuts import render, get_object_or_404

from blog.Post import BlogPost


def index(request):
    context = {}

    context['BlogPosts'] = BlogPost.objects.all()
    return render(request, "blog/index.html", context)
