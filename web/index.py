from django.http import HttpResponse
from django.shortcuts import render

def webpage(request):
    return render(request, "index.html")

def webpage2(request):
    results=respond.GET['Month']
    return render(request, "index2.html", {'Month':results})