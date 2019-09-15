from django.forms import Form
from django import forms


class UrlForm(Form):

    url = forms.CharField(label='RSS URL', max_length=300)

    
    def clean(self):
        cleaned_data = super(UrlForm, self).clean()
        url = cleaned_data.get('url')