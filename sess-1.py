
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from .models import Profile, Actel , Data, Client
from django.http import JsonResponse
from django.template.loader import render_to_string
import datetime
from app.form import ActelForm, ProfileForm ,DataForm
from app.hash import make_hash
from django.db.models import Sum

# Create your views here.
def index(request): 
   if request.method == "POST":
       compteid = request.POST['compteid']
       password = request.POST['apassword']
       apassword = make_hash(password)
       nom = Profile.objects.filter(compteid=compteid).values('nom')[0]['nom']
       role = Profile.objects.filter(compteid=compteid).values('role')[0]['role']
       aid = Profile.objects.filter(compteid=compteid).values('aid')[0]['aid']
       if Profile.objects.filter(compteid=compteid, apassword=apassword).exists():
          request.session['nom'] = nom
          request.session['role'] = role
          request.session['aid'] = aid
          return redirect('home')
       else:
           return render(request, "index.html")
   else:   
       return render(request, "index.html")
    

def dashboard(request):
    all_datas = Data.objects.all()
    return render(request,'dashboard.html', {'Datas': all_datas})


def hom(request):
    return render(request, "hom.html")

def home(request):
    return render(request, "home.html")

def homea(request):
    return render(request, "homea.html")

def homeu(request):
    return render(request, "homeu.html")


def compte(request):
   all_comptes = Profile.objects.all()
   if request.method == "POST":
       compteid = request.POST['compteid']
       nom = request.POST['nom']
       email = request.POST['email']
       service = request.POST['service']
       agence = request.POST['agence']
       role = request.POST['role']
       apassword = make_hash( request.POST['apassword'] )
       
       if Profile.objects.filter(compteid=compteid).exists():
           return redirect('compte')
       elif User.objects.filter(email=email).exists():
           return redirect('compte')
       else:
           compte = Profile.objects.create(compteid=compteid, nom=nom, email=email, service=service, agence=agence, role=role, apassword=apassword)
           compte.save();
           return redirect('compte')
   else:
        return render(request, "compte.html", {'Comptes': all_comptes})



def mcompte(request, cid):
   comptes = Profile.objects.get(compteid=cid)
   if request.method == "POST":
       compteid = request.POST['compteid']
       nom = request.POST['nom']
       email = request.POST['email']
       service = request.POST['service']
       agence = request.POST['agence']
       role = request.POST['role']
       compte = Profile.objects.filter(compteid=cid).update(compteid=compteid, nom=nom, email=email, service=service, agence=agence, role=role)
       return redirect('compte')
   else:
        return render(request,'mcompte.html', {'comptes': comptes})



def dcompte(request, cid):
   compte = Profile.objects.get(compteid=cid)
   compte.delete()
   return redirect('compte')


def agence(request):
   all_agences = Actel.objects.all()
   if request.method == "POST":
       form = ActelForm(request.POST or None)
       if form.is_valid():
          form.save()
          return redirect('agence')
   else:
        return render(request, "agence.html", {'Agences': all_agences})

        
def magence(request, id):
   agences = Actel.objects.get(aid=id)
   form = ActelForm(request.POST or None,instance=agences)
   if form.is_valid():
      form.save(commit=True)
      return redirect('agence') 
   return render(request,'magence.html', {'agences': agences})


def dagence(request, id):
   agence = Actel.objects.get(aid=id)
   agence.delete()
   return redirect('agence')

def client_chart(request):
    labels = []
    data = []

    queryset = Data.objects.values('jour').annotate(nbrclient=Sum('nbrclient')).order_by('-jour')
    for entry in queryset:
        labels.append(entry['jour'])
        data.append(entry['nbrclient'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def att_chart(request):
    labels = []
    data = []

    queryset = Data.objects.values('jour').annotate(attmoy=Sum('attmoy')).order_by('-jour')
    for entry in queryset:
        labels.append(entry['jour'])
        data.append(entry['attmoy'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

