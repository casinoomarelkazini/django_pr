from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Film)
admin.site.register(Seen)
admin.site.register(Tip)
admin.site.register(Like)

