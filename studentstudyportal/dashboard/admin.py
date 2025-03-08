from django.contrib import admin
from .models import*
from .forms import*


# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
