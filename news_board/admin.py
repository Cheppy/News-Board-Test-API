from .models import Article, Comment, Board_User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class Board_User_Inline(admin.StackedInline):
    model = Board_User
    can_delete = False
    verbose_name_plural = "board_users"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Board_User_Inline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Comment)
