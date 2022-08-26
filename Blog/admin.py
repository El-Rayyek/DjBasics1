from django.contrib import admin

# Register your models here.
from .models import post , Category

class AdminPost(admin.ModelAdmin):
    list_display = ['id','title','category']
    search_fields = ['content','title']
    date_hierarchy = 'publish_date'




admin.site.register(post , AdminPost)
admin.site.register(Category)