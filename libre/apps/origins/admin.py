from __future__ import absolute_import

from django.contrib import admin, messages
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import OriginDatabase, OriginFTPFile, OriginUploadedFile, OriginURLFile, OriginPath, OriginRESTAPI, OriginSOAPWebService


class OriginAdmin(admin.ModelAdmin):
    suit_form_tabs = (('configuration', _('Configuration')),)

    fieldsets = (
        (_('Basic information'), {
            'classes': ('suit-tab suit-tab-configuration',),
            'fields': ('label', 'description',)
        }),
    )

    list_display = ('label', 'description')


class OriginDatabaseAdmin(OriginAdmin):
    fieldsets = OriginAdmin.fieldsets + (
        (_('Specific information'), {
            'classes': ('suit-tab suit-tab-configuration',),
            'fields': ('db_backend', 'db_name', 'db_user', 'db_password', 'db_host', 'db_port', 'db_query')
        }),
    )
    list_display = OriginAdmin.list_display + ('db_backend', 'db_name')


class OriginURLFileAdmin(OriginAdmin):
    fieldsets = OriginAdmin.fieldsets + (
        (_('Specific information'), {
            'classes': ('suit-tab suit-tab-configuration',),
            'fields': ('url',)
        }),
    )
    list_display = OriginAdmin.list_display + ('url',)


class OriginPathAdmin(OriginAdmin):
    fieldsets = OriginAdmin.fieldsets + (
        (_('Specific information'), {
            'classes': ('suit-tab suit-tab-configuration',),
            'fields': ('path',)
        }),
    )
    list_display = OriginAdmin.list_display + ('path',)


admin.site.register(OriginDatabase, OriginDatabaseAdmin)
admin.site.register(OriginFTPFile)
admin.site.register(OriginUploadedFile)
admin.site.register(OriginURLFile, OriginURLFileAdmin)
admin.site.register(OriginPath, OriginPathAdmin)
admin.site.register(OriginRESTAPI)
admin.site.register(OriginSOAPWebService)
