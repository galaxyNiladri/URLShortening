from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import URLStore
from django.db import transaction
import hashlib


def shorten_url(input_url):
    original_url = input_url
    unique_url = hashlib.md5(f"{original_url}".encode()).hexdigest()[:10]
    return unique_url


def home(request):
    return render(request, "url_home.html")


def url_short(request):
    context = {}
    if request.method == "POST":
        long_url = request.POST.get('inurl')
        if long_url:
            try:
                with transaction.atomic():
                    short_url = shorten_url(long_url)
                    context["input"] = long_url
                    context["output"] = "https://" + short_url
                    URLStore.objects.create(input_url=long_url, hash_url=short_url)
            except Exception as e:
                transaction.set_rollback(True)
                context["Error"] = f"Failed to shorten url {str(e)}"
        return render(request, "url_template.html", context)
    return render(request, "url_template.html")
