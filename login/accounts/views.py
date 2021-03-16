from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Article
# Create your views here.
@login_required
def dasboardView(request):
    article_list=Article.objects.all()
    return render(request,'dashboard.html',{'article_list':article_list})

def indexView(request):
    return render(request,'index.html')

def registerView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()

    return render(request,'registration/register.html',{'form':form})

