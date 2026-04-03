from django.contrib import admin
from .models import Vet_Officer, Farmer, Farm, Official, User, Farm

admin.site.register(User)
admin.site.register(Vet_Officer)
admin.site.register(Farmer)
admin.site.register(Official)
admin.site.register(Farm)