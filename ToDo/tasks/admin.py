from django.contrib import admin
from tasks.models import task, hashtag

admin.site.register(task)
admin.site.register(hashtag)
