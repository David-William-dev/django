from django.contrib import admin
from .models import Post,Category,ContactData,AboutPage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')
    list_filter = ('category','created_at')
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(ContactData)
admin.site.register(AboutPage)
