from django.shortcuts import render, redirect
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Product
from .forms import ContactForm

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            return redirect('thanks')  # Или другая страница после отправки
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home(request):
    t_shirts = Product.objects.filter(category='t')
    hoodies = Product.objects.filter(category='h')
    return render(request, 'home.html', {
        't-shirts': t_shirts,
        'hoodies': hoodies,
    })

def thanks(request):
    return render(request, 'thanks.html')