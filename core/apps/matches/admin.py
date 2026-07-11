from django.contrib import admin
from .models import Message, Match
# Register your models here.

admin.site.register(Match)
admin.site.register(Message)