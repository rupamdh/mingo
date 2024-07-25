from django.contrib import admin
from .models import *

# from mingo.admin import MingoBaseAdmin
# Register your models here.
# admin.site.register(Book)
admin.site.register(Author)

def make_available(self, request, queryset):
    queryset.update(status=True)
def make_not_available(self, request, queryset):
    queryset.update(status=False)

make_available.short_description = "Mark selected books as available"
make_not_available.short_description = "Mark selected books as not available"

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'status')
    search_fields = ('title', 'price')
    list_filter = ('status', 'author')
    list_per_page = 10
    actions = [make_available, make_not_available]


admin.site.register(Book, BookAdmin)

