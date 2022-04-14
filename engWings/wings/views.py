from django.shortcuts import render
# from sklearn.metrics import mean_gamma_deviance
from .models import Videos
# contactform
import os
import smtplib
# import imghdr
from email.message import EmailMessage
# --------------------------------------------

    #dests=courses.objects.all()
    #return render(request,'index.html',{'dests':dests})

# Create your views here.
def index(request):


    return render(request,'index.html')

#return about page
def about(request):


    return render(request,'about.html')

#return content page
def content(request):
    videos = Videos.objects.all()
    front =Videos.objects.get(title='Introduction')
    

    return render(request,'content.html',{"videos":videos,"front":front})


#return contact page
def contact(request):


    return render(request,'contact.html')
def front(request,title):
    videos = Videos.objects.all()
    front =Videos.objects.get(title=title)

    return render(request,'content.html',{"videos":videos,"front":front})

def contactform(request):
   
    

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    
    email = request.POST['email']
    phone_number=request.POST['phone_number']
    mg = request.POST['message']
        

    EMAIL_ADDRESS = 'nerthinksjareen@gmail.com'
    EMAIL_PASSWORD = 'Ironman@12'

    msg = EmailMessage()
    msg['Subject'] = 'contacting'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    msg.set_content(mg)
    
   
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

   
    return render(request,'contact.html')
        
