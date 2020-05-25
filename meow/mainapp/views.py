from django.shortcuts import render

def main(request):
    return render(request, "mainapp/index.html")

def meow(request):
    return render(request, "mainapp/meow.html")
