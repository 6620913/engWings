from django.shortcuts import render
from .models import Videos
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

    return render(request,'content.html',{"video":videos})


#return contact page
def contact(request):


    return render(request,'contact.html')
