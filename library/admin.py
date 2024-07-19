from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Book)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'status')
    search_fields = ('title', 'price')


admin.site.register(Book, BookAdmin)