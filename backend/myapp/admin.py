from django.contrib import admin
from .models import Todo, user
# Register your models here.


class userAdmin(admin.ModelAdmin):
    pass


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
admin.site.register(user, userAdmin)
