from django.contrib import admin
from .models import *

# from mingo.admin import MingoBaseAdmin
# Register your models here.
# admin.site.register(Book)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'status')
    search_fields = ('title', 'price')
    list_filter = ('status', 'author')
    list_per_page = 10


admin.site.register(Book, BookAdmin)

