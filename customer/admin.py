from django.contrib import admin

# Register your models here.
from .models import Custinfo,Contact,Custom_order

admin.site.register(Custinfo)
admin.site.register(Contact)
admin.site.register(Custom_order)