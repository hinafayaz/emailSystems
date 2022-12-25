from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from Eemail.models import Message
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,'Eemail/index.html')
def sendmail(request):
    email=Message.objects.get('recipient')
    subject="welcome to my email "
    message="this is ur emailsystem "
    email_from= settings.EMAIL_HOST_USER
    reciever=[email,]
    send_mail(subject,message,email_from,reciever)
    return redirect("home")
