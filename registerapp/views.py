from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registerkoclasshaita
from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.
def homes(request):
  if request.method == "POST":
    username_rakha= request.POST['username_rakha']
    email_rakha= request.POST['email_rakha']
    password_rakha= request.POST['password_rakha']
    password_thikcha = request.POST['password_thikcha']
    user = Registerkoclasshaita(username_rakha = username_rakha,email_rakha=email_rakha,password_rakha =password_rakha,password_thikcha=password_thikcha)
    user.save()
    messages.success(request,"data haru sabbai gayo hai ta")
  return render(request,'register.html')
def datadekhau(request):
    dataharu = Registerkoclasshaita.objects.all()
    return render(request,"datashow.html",{'data':dataharu})
  
def data_faldeu(request,id):
   dataharu = Registerkoclasshaita.objects.get(id = id)
   dataharu.delete()
   messages.success(request,"data haru sabbai delete vayo hai ta!")
   return render(request,"datashow.html")

class Editdata(UpdateView):
    model = Registerkoclasshaita
    template_name = "edit.html"
    fields = ['username_rakha', 'email_rakha', 'password_rakha', 'password_thikcha']
    success_url = reverse_lazy('datashow')


  
  