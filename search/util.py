import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# extract titles Rijksmuseum from data
def get_longtitle(conts_new):
    content = []
    for item in range(len(conts_new['artObjects'])):
        content.append(conts_new['artObjects'][item]['longTitle'])
    return content

# extract images Rijksmuseum from data, if no image, use "no image available"
def get_images(conts_new):
    imagesurl = []
    for item in range(len(conts_new['artObjects'])):
        if conts_new['artObjects'][item]['hasImage']:
            imagesurl.append(conts_new['artObjects'][item]['webImage']['url'])
        else:
            imagesurl.append("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg")
    return imagesurl

# extract titles Cleveland Museum of Art from data
def get_title_clev(content_clev_new):
    content = []
    for item in range(len(content_clev_new['data'])):
        content.append(content_clev_new['data'][item]['tombstone'])
    return content

# extract images Cleveland Museum of Art from data
def get_image_clev(content_clev_new):
    imagesurl = []
    for item in range(len(content_clev_new['data'])):
        imagesurl.append(content_clev_new['data'][item]['images']['web']['url'])
    return imagesurl
