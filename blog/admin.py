from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    pass

class InfoBlockAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(InfoBlockModel, InfoBlockAdmin)
admin.site.register(PostModel, PostAdmin)