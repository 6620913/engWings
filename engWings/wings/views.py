from django.shortcuts import render
# from sklearn.metrics import mean_gamma_deviance
from .models import Videos,Courses
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
    front = Videos.objects.get(course_id=0)

    return render(request,'index.html',{"front":front})

#return about page
def about(request):


    return render(request,'about.html')

#return content page
def content(request,course_id):
    content = Videos.objects.filter(course_id=course_id).order_by("cvs")
    front = content[0]
    ctitle = Courses.objects.get(course_id=course_id)
    

    return render(request,'content.html',{"content":content,"front":front,"ctitle":ctitle})


#return contact page
def contact(request):


    return render(request,'contact.html')

def front(request,id,course_id):
    content = Videos.objects.filter(course_id=course_id).order_by("cvs")
    front = Videos.objects.get(id=id)
    ctitle = Courses.objects.get(course_id=course_id)
    

    return render(request,'content.html',{"content":content,"front":front,"ctitle":ctitle})
    
   

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
        
# return courses page with courses data
def courses(request):
    courses = Courses.objects.all()
    

    return render(request,'courses.html',{"courses":courses})