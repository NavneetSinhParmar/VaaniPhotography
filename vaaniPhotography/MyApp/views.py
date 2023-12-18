from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request,"contact.html")

def wedding_view(request):
    return render(request,"wedding.html")

def pre_wedding_view(request):
    return render(request,"pre_wedding.html")

def meternity_view(request):
    return render(request,"meternity.html")

def baby_born_view(request):
    return render(request,"baby_born.html")

def baby_photoshoot_view(request):
    return render(request,"baby_photoshoot.html")

def album_view(request):
    return render(request,"album.html")

def video_view(request):
    return render(request,"video.html")