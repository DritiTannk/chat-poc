from django.contrib import admin
from .models import *


class BotResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender',
                    'user_msg', 'polly_file',
                    'created', 'modified'
                    )


admin.site.register(BotResponse, BotResponseAdmin)
