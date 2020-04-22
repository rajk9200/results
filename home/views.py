from django.shortcuts import render

# Create your views here.
from Posts.models import Posts,PostCot
def home(request):
    cat_res =PostCot.objects.get(name="Results")
    resposts =Posts.objects.filter(title=cat_res)
    context ={
        'resposts':resposts,
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contacts.html')