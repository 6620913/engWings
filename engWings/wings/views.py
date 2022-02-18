from django.shortcuts import render

# Create your views here.
def index(request):


    #dests=courses.objects.all()
    #return render(request,'index.html',{'dests':dests})
    return render(request,'index.html')

