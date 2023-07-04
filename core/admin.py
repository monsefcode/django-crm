from django.contrib import admin
from core.models import Profile

# Register your models here.
admin.site.site_header = "CRM Admin"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'address', 'phone')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'user__email')

admin.site.register(Profile, ProfileAdmin)