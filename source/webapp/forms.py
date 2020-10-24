from django import forms
from webapp.models import Photo


class PhotoCreateForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'signature']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'signature', 'author']