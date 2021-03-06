#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0 Beta
@author: Deepak
@license: MIT Licence
@contact: medgloss@gmail.com
@site: https://www.medgloss.com/
@software: Visual Studio Code
@file: admin_site.py
"""
from servermanager.admin import *
from django.contrib.admin import AdminSite
from Medgloss.utils import get_current_site
from django.contrib.sites.admin import SiteAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.sites.models import Site
from Medgloss.logentryadmin import LogEntryAdmin
from blog.admin import *
from accounts.admin import *
from oauth.admin import *

from comments.admin import *



class MedglossAdminSite(AdminSite):
    site_header = 'Medgloss administration'
    site_title = 'Medgloss site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser

    # def get_urls(self):
    #     urls = super().get_urls()
    #     from django.urls import path
    #     from blog.views import refresh_memcache
    #
    #     my_urls = [
    #         path('refresh/', self.admin_view(refresh_memcache), name="refresh"),
    #     ]
    #     return urls + my_urls


admin_site = MedglossAdminSite(name='admin')

admin_site.register(Article, ArticlelAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Links, LinksAdmin)
admin_site.register(SideBar, SideBarAdmin)
admin_site.register(BlogSettings, BlogSettingsAdmin)



admin_site.register(BlogUser, BlogUserAdmin)

admin_site.register(Comment, CommentAdmin)

admin_site.register(OAuthUser, OAuthUserAdmin)
admin_site.register(OAuthConfig, OAuthConfigAdmin)

admin_site.register(EmailSendLog, EmailSendLogAdmin)

admin_site.register(Site, SiteAdmin)

admin_site.register(LogEntry, LogEntryAdmin)



