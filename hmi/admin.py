from django.contrib import admin
from .models import Hmi

@admin.register(Hmi)
class HmiAdmin(admin.ModelAdmin):
    
    list_display = ["title", "author", "createdDate"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    class Meta:
        model = Hmi