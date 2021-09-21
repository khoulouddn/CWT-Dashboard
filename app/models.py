from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Actel(models.Model):
    aid = models.AutoField(primary_key=True)
    agenceid = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    nbragent = models.IntegerField()
    isactive = models.BooleanField(default=False)
    
class Profile(models.Model):
    profileid = models.AutoField(primary_key=True) 
    compteid = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    agence = models.CharField(max_length=100)
    apassword = models.CharField(max_length=100)
    aid = models.ForeignKey(Actel, on_delete=models.SET_NULL, null=True)
class Role(models.Model):
    rid = models.AutoField(primary_key=True)
    simpleuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superadmin = models.BooleanField(default=False)

class Fontionnalite(models.Model):
    fid = models.AutoField(primary_key=True)
    gerercompte = models.BooleanField(default=False)
    gereragence = models.BooleanField(default=False)

 
class Client(models.Model):
    cid = models.AutoField(primary_key=True)
    clientid = models.CharField(max_length=50)
    jour = models.DateField(null=True, blank=True)
    timee = models.DateTimeField()
    timel = models.DateTimeField()
    times = models.IntegerField()
    aid = models.ForeignKey(Actel, on_delete=models.SET_NULL, null=True)

class Data(models.Model):
    did = models.AutoField(primary_key=True)
    jour = models.DateField(null=True, blank=True)
    nbragent = models.IntegerField()
    nbrclient = models.IntegerField()
    attmoy = models.IntegerField()
    maxt = models.IntegerField()
    mint = models.IntegerField()
    aid = models.ForeignKey(Actel, on_delete=models.SET_NULL, null=True)


class Peut(models.Model):
    peutid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    rid = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class Possed(models.Model):
    possedid = models.AutoField(primary_key=True)
    rid = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    fid = models.ForeignKey(Fontionnalite, on_delete=models.SET_NULL, null=True)


class Gerer(models.Model):
    gererid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    aid = models.ForeignKey(Actel, on_delete=models.SET_NULL, null=True)





