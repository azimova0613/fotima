from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    context={
        "story":story.objects.all(),
        "story2":story2.objects.all(),
        "story3":story3.objects.all(),
        "story4":story4.objects.all(),
        "story5":story5.objects.all(),
        "story6":story6.objects.all(),
        "story7":story7.objects.first(),
        "story8":story8.objects.first(),
        "story9":story9.objects.all(),
        "story14":story14.objects.all(),
        "story15":story15.objects.first(),
        "story16":story16.objects.all(),
        "story17":story17.objects.first(),
        "story18":story18.objects.all(),
        "story21":story21.objects.first(),
        "story22":story22.objects.first(),
        

        
        

    }
    return render(request,'index.html',context)


def shop (request):
    context={
        "shop1":shop1.objects.first(),
        "story14":story14.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first()


    }
    return render(request,'shop.html',context)


def contact(request):
    if request.method == 'POST':
    
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone=request.POST['Phone']
        massage=request.POST['massage']

        kantakt2.objects.create(Username=Username,Email=Email,Phone=Phone,massage=massage)
    context={
        "kantak":kantak.objects.first(),
        "story20":story20.objects.first(),
        "story19":story19.objects.first(),


    }
    return render(request,'contact.html',context)


def blogsingle(request):
    if request.method == 'POST':
        
            text=request.POST['text']
            ism=request.POST['ism']
            mavzu=request.POST['mavzu']
            email=request.POST['email']
    
            izoh.objects.create(text=text,ism=ism,mavzu=mavzu,email=email)
    context={
        "march":march.objects.first(),
        "camment":camment.objects.all(),
        "post":post.objects.all(),
        "post2":post2.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),
        
       

    }
    return render(request,'blog-single.html',context)

def gallery(request):
    context={
        "story9":story9.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),



       

    }
    return render(request,'gallery.html',context)

def team(request):
    context={
        "story16":story16.objects.all(),
       

    }
    return render(request,'team.html',context)

def service(request):
    context={
        "story4":story4.objects.all(),
        "story5":story5.objects.all(),
        "story6":story6.objects.first(),
        "story2":story2.objects.all(),
        "story3":story3.objects.all(),
        "story":story.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),
       

    }
    return render(request,'services.html',context)

def shopsingle(request):
    context={
        "xarid":xarid.objects.first(),
        "xarid2":xarid2.objects.first(),
        "xarid3":xarid3.objects.first(),
        "story14":story14.objects.all(),
        "loyiha":loyiha.objects.all(),
        "story9":story9.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),
      
        # "story16":story16.objects.all(),

       

    }
    return render(request,'shop-single.html',context)

def errorpage(request):
    context={
        "page":page.objects.first(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),
        #"story16":story16.objects.all(),
       

    }
    return render(request,'error-page.html',context)

def teamsingle(request):
    context={
        "jamoa":jamoa.objects.first(),
        "jamoa2":jamoa2.objects.first(),
        "dehqon":dehqon.objects.first(),
        "story16":story16.objects.all(),
        "story19":story19.objects.first(),
        "story20":story20.objects.first(),
       

    }
    return render(request,'team-single.html',context)