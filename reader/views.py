from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .forms import UrlForm
import feedparser
from bs4 import BeautifulSoup
import requests
import re

def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():

            url = form.cleaned_data['url']

            feeds = feedparser.parse(url)

            all_feeds = []

            for feed in feeds.entries:
                link = feed.link.rsplit('/')
                new_link = ""
                for i in range(2,len(link)):
                    new_link = new_link + '--' + link[i]
                    new_link = new_link.replace("--www.","")

                all_feeds.append({
                    'title' : feed.title,
                    'link' : new_link,
                    'description' : feed.description,
                    'published' : feed.published
                })

            return render(request, 'allfeeds.html', {'data' : all_feeds})

    else:
        form = UrlForm()

    return render(request, 'home.html', {'form': form})

def detail(request, link):
    link = link.replace("--","/")
    link = 'http://www.'+link

    source = requests.get(link)

    soup = BeautifulSoup(source.text, 'html.parser')

    data = {
        'image' : soup.find("meta",  property="og:image")["content"],
        'title' : soup.find("meta",  property="og:title")["content"],
        'description' : soup.find("meta",  property="og:description")["content"]
    }

    return render(request, 'detail.html', data)