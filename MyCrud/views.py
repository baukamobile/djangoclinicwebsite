from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import BlogPostForm, UploadForm
from .models import BlogPost
from .serializers import BlogSerializer
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import ssl
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

    return render(request, 'wg_early_bird_template/index.html', context={
        'task': blog,
        'form': form,
    })



def upload(request):
    uploadform = UploadForm(request.POST, request.FILES)
    if request.POST:
        print(request.FILES)
        if uploadform.is_valid():
            uploadform.save()
    return render(request, 'wg_early_bird_template/upload.html',context={
        'uploadform': uploadform,
    })


def blog(request):
    blog = BlogPost.objects.all()
    serializer = BlogSerializer()
    return JsonResponse(serializer.data)

# def send_email(request):
#     if request.method=='POST':
#         message = request.POST['message']
#         email = request.POST['email']
#         name = request.POST['name']
#         send_mail(
#             'Contact_mail',
#             message,
#             'settings.EMAIL_HOST_USER',
#             [email],
#             fail_silently=False
#         )
#         return render(request, 'wg_early_bird_template/index.html')

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "baukabakbergen003@gmail.com",
#     ["bauyrzanbakbergen87@gmail.com"],
#     fail_silently=False,
# )
#bauyrzanbakbergen87@gmail.com
#'bauyrzanbakbergen87@gmail.com', 'newnewernewest123@gmail.com'
# def send_email_view(request):
#     subject = 'Hello from MoneyApp'
#     message = 'You are succefully authenticated!'
#     sender = 'baukabakbergen003@gmail.com'
#     recipient_list = ['bauyrzanbakbergen87@gmail.com', 'newnewernewest123@gmail.com']

#     try:
#         send_mail(subject, message, sender, recipient_list)
#         return HttpResponse("Email sent successfully")
#     except Exception as e:
#         return HttpResponse(f"An error occurred: {str(e)}")


def showPage(request):
    return render(request, 'clinic-website-template/index.html')
