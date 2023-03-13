from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("advanced", views.advanced, name="advanced"),
    path("collections", views.collections, name="collections"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("searchres", views.searchres, name="searchres"),
    path("adsearchres", views.adsearchres, name="adsearchres")
]
