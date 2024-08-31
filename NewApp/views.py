from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("আপনার বাড়ি কোথায় !!??")
    return render(request, "product/homepage.html", {})