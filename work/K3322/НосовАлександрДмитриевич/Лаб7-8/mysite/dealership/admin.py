from django.contrib import admin
from .models import Product
from .models import ContactMessage

admin.site.register(Product)
admin.site.register(ContactMessage)