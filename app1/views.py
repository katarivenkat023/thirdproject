from django.shortcuts import render, HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<h1><marquee>this is my first views</h1>")

def venkat(request):
    return HttpResponse('<h1 style=color:blue;><marquee>venkat python developer</h1>')
