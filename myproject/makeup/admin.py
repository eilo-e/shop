from django.contrib import admin

from.models import Shop
admin.site.register(Shop)

from.models import User
admin.site.register(User)

from.models import Makeup
admin.site.register(Makeup)

from.models import Skincare
admin.site.register(Skincare)

from.models import Digitalstuff
admin.site.register(Digitalstuff)

from.models import Sell
admin.site.register(Sell)

class SkincareAdmin(admin.ModelAdmin):
    list_display = ['id','productname','shopename','brandname']

class MakeupAdmin(admin.ModelAdmin):
    list_display = ['id','productname','shopename','brandname']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','shopname','city','shopPhoneNumber']

class DigitalstuffAdmin(admin.ModelAdmin):
    list_display = ['id','productname','shopename','brandname']

