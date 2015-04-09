from django.contrib import admin
from west.models import Character, Contact, Tag


class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
        
    )
    search_fields = ['name',]
    list_display = ('name','age', 'email') # list

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
