from django.contrib import admin

# Register your models here.
from FormGen.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['order', 'team', 'name', 'sex', 'age', 'community', 'contact']


admin.site.register(Person, PersonAdmin)