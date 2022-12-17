from django.contrib import admin
from .models import UserProfileInfo, Kategori, Film, Comment

@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'nama']

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug')
    list_filter = ('nama', 'slug')
    search_fields =  ('nama', 'slug')
    prepopulated_fields= {'slug': ('nama,')}

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('nama', 'slug', 'deskripsi', 'created', 'updated')
    list_filter = ('deskripsi', 'created', 'updated')
    search_fields =  ('nama', 'slug')
    prepopulated_fields= {'slug': ('nama,')}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nama', 'body', 'post', 'created')
    list_filter = ('post', 'created')
    search_fields =  ('nama', 'body')
    actions = ['approve_comments']
