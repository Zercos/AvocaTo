from django.contrib import admin

from quest import models

admin.site.register(models.Question)
admin.site.register(models.Answer)
