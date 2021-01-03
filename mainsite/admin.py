from django.contrib import admin
from mainsite.models import Post,company
admin.site.register(Post)

class companyadmin(admin.ModelAdmin):
    list_display = ('time','place','people','car','longitude','latitude')
admin.site.register(company,companyadmin)
# Register your models here.
