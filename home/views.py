from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is homepage(/)")
    #context={'name':' KT Harry','course':' python Django'}
    #return render(request, 'home.html',context)
    return render(request, 'home.html')


def about(request):
    #return HttpResponse("This is aboutpage(/about)")
    return render(request, 'about.html')


def projects(request):
    #return HttpResponse("This is projectspage(/)")
    return render(request, 'projects.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        contact = Contact(name= name,email= email,phone= phone,desc= desc)
        contact.save()
        print("Data is in DB")
        
    return render(request, 'contact.html')
        #return HttpResponse("This is contactpage(/)")

