from django.contrib import admin

# Register your models here.
# import your model
from collection.models import Users

class UsersAdmin(admin.ModelAdmin):
	model = Users
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

	# and register it
admin.site.register(Users, UsersAdmin)