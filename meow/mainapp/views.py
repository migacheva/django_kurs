from django.shortcuts import render

def main(request):
    return render(request, "mainapp/index.html")

def meow(request):
    return render(request, "mainapp/index2.html")

def univer(request):
    return render(request, "mainapp/univer.html")

def job(request):
    return render(request, "mainapp/job.html")
