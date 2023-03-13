from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown
import requests
import json

from . import util

# display main home and search page
def index(request):
    return render(request, "search/index.html", {
    })

# display advanced search page
def advanced(request):
    return render(request, "search/advanced.html", {
    })

# display page stating which collections included
def collections(request):
    return render(request, "search/collections.html", {
    })

# display page on the project
def about(request):
    return render(request, "search/about.html", {
    })

# display page providing contact details
def contact(request):
    return render(request, "search/contact.html", {
    })

# render page that shows search results of "quick search"
def searchres(request):
    if request.method == "POST":
        q = request.POST["q"]

        # request to Rijksmuseum, and extraction of data
        content = requests.get(f'https://www.rijksmuseum.nl/api/en/collection?key=8gLRCRyO&q={q}&ps=100&p=0-10')
        cont_new = content.json()
        content2 = util.get_longtitle(cont_new)
        images = util.get_images(cont_new)
        content = dict(zip(content2, images))

        # request to Cleveland Museum of Art, and extraction of data
        content_clev = requests.get(f'https://openaccess-api.clevelandart.org/api/artworks?q={q}&limit=50&has_image=1')
        content_clev_new = content_clev.json()
        content_clev2 = util.get_title_clev(content_clev_new)
        content_clev2_im = util.get_image_clev(content_clev_new)
        content_display_clev = dict(zip(content_clev2, content_clev2_im))

        # add two dicts into one list
        content_page = [content, content_display_clev]
        return render(request, "search/searchres.html", {
        'content': content_page
        })

# render page that displays advanced search results
def adsearchres(request):
    if request.method == "POST":
        q = request.POST["q"]
        object = request.POST["object"]
        title = request.POST["title"]
        fromm = request.POST["from"]
        to = request.POST["to"]

        # request to Rijksmuseum, and extraction of data
        content = requests.get(f'https://www.rijksmuseum.nl/api/en/collection?key=8gLRCRyO&involvedMaker={q}&ps=100&p=0-10&type={object}&title={title}&yearfrom={fromm}&yearto={to}')
        cont_new = content.json()
        content2 = util.get_longtitle(cont_new)
        images = util.get_images(cont_new)
        content = dict(zip(content2, images))

        # request to Cleveland Museum of Art, and extraction of data
        object2 = object.capitalize()
        content_clev = requests.get(f'https://openaccess-api.clevelandart.org/api/artworks?artists={q}&limit=50&has_image=1')
        content_clev_new = content_clev.json()
        content_clev2 = util.get_title_clev(content_clev_new)
        content_clev2_im = util.get_image_clev(content_clev_new)
        content_display_clev = dict(zip(content_clev2, content_clev2_im))

        # add two dicts into one list
        content_page = [content, content_display_clev]
        return render(request, "search/adsearchres.html", {
        'q': q,
        'object': object,
        'title': title,
        'fromm': fromm,
        'to': to,
        'content': content_page
        })
