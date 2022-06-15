from django.contrib import admin
from .models import Prommies, Profile

admin.site.register(Prommies)
admin.site.register(Profile)

# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'prommies', 'text', 'rate')
#     readonly_fields = ['created_at']