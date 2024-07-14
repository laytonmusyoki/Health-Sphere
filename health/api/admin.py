from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Token)
admin.site.register(OtpCode)
admin.site.register(Workouts)
admin.site.register(Feeds)
