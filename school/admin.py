from django.contrib import admin
from .models import Time
# Register your models here.
class TimeAdmin(admin.ModelAdmin):
	list_display = ['name1', 'name2', 'name3', 'name4', 'time', 'court']
	list_filter = ['court']
	list_editable = ['time']


admin.site.register(Time, TimeAdmin)

# Register your models here.
