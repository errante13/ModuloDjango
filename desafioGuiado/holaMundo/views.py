from django.shortcuts import render

# Create your views here.
def inicio(request):
     return render(request,'inicio.html')

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')