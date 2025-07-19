from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
from app.models import Event, Testimonial, Gallery, Cabinet, Course

def home(request):
    events = Event.objects.all()
    testimonials = Testimonial.objects.all()[:3] 
    return render(request, 'index.html', {'events': events, 'testimonials': testimonials})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def gallery(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery.html', {'galleries': galleries})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')
    return render(request, 'index.html')

def cabinet_list(request):
    cabinets = Cabinet.objects.all()
    return render(request, 'cabinet_list.html', {'cabinets': cabinets})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})