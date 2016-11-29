from django.contrib import admin
from .models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name","status") # show different fields

    #tuple must have a "," in the end!!!
admin.site.register(Block, BlockAdmin)

#admin.site.register(Block)
