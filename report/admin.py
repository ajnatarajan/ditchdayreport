from django.contrib import admin

from .models import User, Report


# def is_ugne_slug():
# return True
# Register your models here.

admin.site.register(User)
admin.site.register(Report)
