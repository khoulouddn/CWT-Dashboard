from django import forms
from app.models import Profile, Actel, Data

class ActelForm(forms.ModelForm):
    class Meta:
        model = Actel
        fields = ['agenceid','nom','adress','nbragent']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['compteid','service','email','nom','role','agence','apassword']


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['jour','nbragent','nbrclient','attmoy','maxt','mint']

