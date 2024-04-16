from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.
# def showPost(request):
#     blog = BlogPost.objects.all()
#     form = BlogPost()
#     return render(request, 'index.html', context={
#         'form':form,
#         'blog': blog
#     })


def create_new_task(request):
    blog = BlogPost.objects.all()
    form = BlogPostForm()

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_new_task')
        else:
            print(form.errors)

    return render(request, 'index.html', context={
        'task': blog,
        'form': form,
    })



