from django.contrib import admin
from .models import Job,Interest_url,Non_Interest_url
# Register your models here.
admin.site.register(Job)
admin.site.register(Interest_url)
admin.site.register(Non_Interest_url)