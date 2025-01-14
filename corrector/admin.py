from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Correction


@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'original_text', 'corrected_text')
    search_fields = ('user__username', 'original_text', 'corrected_text')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)