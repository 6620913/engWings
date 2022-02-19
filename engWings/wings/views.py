from django.shortcuts import render

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


    return render(request,'content.html')


#return contact page
def contact(request):


    return render(request,'contact.html')
