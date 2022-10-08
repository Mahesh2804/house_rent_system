from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactUs
from django.core.mail import send_mail
from django.conf import settings


def indexpage(request):
    return render(request, "index.html", {})


def gallery(request):
    return render(request, "gallery.html", {})

def gallerypage2(request):
    return render(request, "gallerypage2.html", {})

def gallerypage3(request):
    return render(request, "gallerypage3.html", {})


def contact(request):
    return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})





def houses_home(request):
    return render(request, "houses_home.html", {})


def vehicles_home(request):
    return render(request, "vehicles_home.html", {})


def contact_us(request):
    if request.method == 'POST':
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            post = ContactUs()
            post.fullname= request.POST.get('fullname')
            post.email = request.POST.get('email')
            post.phone = request.POST.get('phone')
            post.message = request.POST.get('message')
            post.save() 

            message = "Hello {}, \n\n We've received your message. Thanks for reaching us !!!".format(post.fullname)
            send_mail("Rental World - Contact", message, settings.EMAIL_HOST_USER, [post.email]) 
            return render(request, 'index.html')  
    else:
        return render(request,'contact.html')