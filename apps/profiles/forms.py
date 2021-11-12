from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'url',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['bio'].widget.attrs.update({
                "maxlength": "300",
                "placeholder": "Enter your bio",
                'class': "textarea"
        })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['url'].widget.attrs.update({
                "placeholder": "Url address",
                'class': "input"
        })

     
