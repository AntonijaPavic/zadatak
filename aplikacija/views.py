from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Eksterijer, Interijer, Posts,Detail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

# Create your views here.

def start(request):
    context={
            "posts":Posts.objects.all()
    }
    return render(request,"aplikacija/start.html",context)
    

def about_us(request):
    context={
            "nama":Interijer.objects.all()
    }
    return render(request,"aplikacija/about_us.html",context)

def interijer(request):
    context={
            "post":Interijer.objects.all()
    }
    return render(request,"aplikacija/interijer.html",context)

def eksterijer(request):
    context={
            "ekst":Eksterijer.objects.all()
    }
    ordering=["-date"]
    return render(request,"aplikacija/eksterijer.html",context)

def save_posts(request):
    return HttpResponse("hooll")

class SinglePostView(DetailView):

    def get(self,request,slug):
        post=Detail.objects.get(slug=slug)
        context={
            "post":post,
        }
        return render(request,"aplikacija/post-detail.html", context)


    def post(self,request,slug):
        post=Detail.objects.get(slug=slug)
        context={
            "post":post,
        }
        return render(request,"aplikacija/post-detail.html", context)
        




class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts=Detail.objects.filter(id__in=stored_posts)
            context["posts"]=posts
            context["has_posts"]=True
        return render(request,"aplikacija/stored_posts.html",context)


        

    
    def post(self,request):
        stored_posts=request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts=[]
        post_id= int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"]=stored_posts
        return HttpResponseRedirect("/")