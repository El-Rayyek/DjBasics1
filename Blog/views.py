from winreg import DeleteValue
from django.shortcuts import render , redirect

# Create your views here.
from .models import post
from .forms import PostForm

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

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request,'blog/new_post.html',{'form':form})

def edit_post(request,id):
    Post = post.objects.get(id = id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=Post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=Post)

    return render(request,'blog/new_post.html',{'form':form})

def delete_post(request,id):
    Post = post.objects.get(id=id)
    Post.delete()
    return redirect('/Blog')

#------------------------------------
# from django.views.generic import ListView , DetailView ,DeleteView
# class Post_view(ListView):
#     model = post

# class Post_Detail(DetailView):
#     model = post

# class Post_Delete(DeleteView):
#     model = post
#     success_url = '/Blog/cbv'
