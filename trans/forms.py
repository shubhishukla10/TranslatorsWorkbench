from django import forms
#from .models import Post

TRANSLATORS = ['Microsoft','Google','IBM']

class PostForm(forms.Form):
    english_text = forms.CharField(widget=forms.Textarea ,label= "Enter text")
    google_trans = forms.BooleanField(label = "Google Translator",required=False)
    sys_trans = forms.BooleanField(label = "Systran Translator",required=False)
    microsoft_trans = forms.BooleanField(label = "Microsoft Translator",required=False)
    ibm_trans = forms.BooleanField(label = "IBM Translator",required=False)
