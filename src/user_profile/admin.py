from django.contrib import admin

from user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'birth_date', 'phone')
    search_fields = ('country',)
    list_filter = ("country",)
    list_editable = ('phone', 'birth_date')
