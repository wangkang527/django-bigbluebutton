# coding: utf-8

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from bbb.models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name','id') 
    list_filter = ['name', 'user']
    search_fields = ['name','user' ]

admin.site.register(Meeting, MeetingAdmin)
