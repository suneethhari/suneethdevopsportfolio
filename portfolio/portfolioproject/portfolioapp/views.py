from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contactform



# Create your views here.
def demo(request):
    return render(request,"index.html")
def single(request):
    return render(request,"single.html")

def contact_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        contactform=contact_form(name=name,email=email,subject=subject,msg=msg)
        contactform.save()
    return render(request,'index.html')
