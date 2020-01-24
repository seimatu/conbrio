from django.contrib import admin

# Register your models here.
from .models import Category,Plan,City,service

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class PlanAdmin(admin.ModelAdmin):
    list_display=('id','plan_title','plan_categories','city_name')
    list_display_links=('id','plan_title')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Plan,PlanAdmin)
admin.site.register(City)
admin.site.register(service)