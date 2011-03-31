#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from mysite.list.models import Article,Shop,New,Message

class ArticleAdmin(admin.ModelAdmin):
    list_display=('num','name','img','node','hoter')
    list_filter=('hoter',)
    search_field=('num','name')
    field=('num','name','img','node')

class ShopAdmin(admin.ModelAdmin):
    list_display=('name','img','node','hoter')
    list_filter=('hoter',)
    field=('name','img','node')

    
class NewAdmin(admin.ModelAdmin):
    list_display=('name','writer','wtime','content','hoter')
    list_filter=('hoter',)
    field=('name','write','wtime','content')

class MessageAdmin(admin.ModelAdmin):
    list_display=('sub','content','name')
    

admin.site.register(Article,ArticleAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Message,MessageAdmin)