from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

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

def contact_us(request):
    if request.method == 'POST':
        # Assuming you have a form for the contact us page
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name,email,phone,message)
        
        # Send email
        send_mail(
            'Contact Us Form Submission',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
            settings.EMAIL_HOST_USER,  # Sender's email
            [settings.YOUR_CONTACT_EMAIL],  # Receiver's email
            fail_silently=False,
        )
        # Redirect or render success page after sending the email
        # Add your logic here
    return render(request, 'contact_us.html')