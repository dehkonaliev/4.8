from django.contrib import admin
from .models import Book, Printing, Genre

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'printing', 'genre']
    list_filter = ['printing', 'genre']
    search_fields = ['title', 'summary']

admin.site.register(Book, BookAdmin)
admin.site.register(Printing)
admin.site.register(Genre)
