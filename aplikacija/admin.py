from django.contrib import admin
from .models import Eksterijer, Posts
from .models import Interijer
from .models import Eksterijer
from .models import Detail
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class InterijerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class EksterijerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class DetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Interijer, InterijerAdmin)
admin.site.register(Eksterijer,EksterijerAdmin)
admin.site.register(Detail,DetailAdmin)