from django.contrib import admin

# Register your models here.
from .models import post , Category

class PostAdmin(admin.ModelAdmin):
    list_display= ['id','title','category']
    search_fields= ['title','content']
    date_hierarchy= ['publish_date']


admin.site.register(post,PostAdmin)
admin.site.register(Category)