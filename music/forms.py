from django import forms
from music.models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'
        #field = ['salutation', 'first_name', 'last_name', 'email']
