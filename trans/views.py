from django.shortcuts import render
from django.utils import timezone
#from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from googletrans import Translator
import json
import requests

url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

headers = {
    'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
    'x-rapidapi-key': "1890d1bc28mshaa8527188a0d1c6p1ffd9cjsn06397720bed5"
    }


# Create your views here.

def post_hello(request):
    #return render(request, 'trans/post_hello.html',{'post':post})
    return render(request, 'trans/post_hello.html')

def post_trans(request):
    translator= Translator()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            english_text = cd['english_text']
            google = cd['google_trans']
            systran = cd['sys_trans']
            microsoft = cd['microsoft_trans']
            ibm = cd['ibm_trans']
            systran_res = "No Translation"
            google_res = "No Translation"
            microsoft_res = "No Translation"
            ibm_res = "No Translation"
            if systran == 1:
                querystring = {"source":"en","target":"hi","input":english_text}
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = response.json()
                systran_res = data['outputs'][0]['output']
            if google == 1:
                google_res = translator.translate(english_text, dest = 'hi').text
            return render(request, 'trans/post_hello.html', {'english_text':english_text,'google_res':google_res,'systran_res':systran_res, 'microsoft_res':microsoft_res, 'ibm_res':ibm_res})
            #return redirect('post_hello')
    else:
        form = PostForm()
    return render(request, 'trans/post_trans.html', {'form':form})
