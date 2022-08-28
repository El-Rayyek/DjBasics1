from django.shortcuts import render

# Create your views here.
from .models import post

'''
    view :
            - url
            - model
            - templates
'''


def post_list(request):
    all_posts = post.objects.all()

    context = {'posts':all_posts}
    return render(request,'blog/post_list.html',context)


def post_detail(request , id):
    Post = post.objects.get(id=id)
    context = {'post':Post}
    return render(request,'blog/post_detail.html',context)