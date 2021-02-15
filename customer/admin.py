from django.contrib import admin

# Register your models here.
from .models import Custinfo,Contact

admin.site.register(Custinfo)
admin.site.register(Contact)