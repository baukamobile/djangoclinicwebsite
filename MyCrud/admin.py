from django.contrib import admin
from .models import *

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
             'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
# Register your models here.


admin.site.register(BlogPost)
admin.site.register(UserAuth)
admin.site.register(SearchItem)