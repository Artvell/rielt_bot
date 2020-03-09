from django.contrib import admin
from Rielt.models import Sale,Rent,Users,Admins,New_builds
# Register your models here.

class SaleAdmin(admin.ModelAdmin):
    list_display=("uid","district","street","orient","room_number","floor","square","condition_of_repair","mater","price","telephon_number","name","status","dop_id")

class RentAdmin(admin.ModelAdmin):
    list_display=("uid","district","street","orient","room_number","floor","square","condition_of_repair","furniture","price","telephon_number","name","status")

class NewAdmin(admin.ModelAdmin):
	list_display=("uid","district","street","builder","reput","compl","date","price","ostat","parking","security","child","struct","uprava","phone","dop_id")
    
class UserAdmin(admin.ModelAdmin):
    list_display=('name','phone','status')

class AdminsAdmin(admin.ModelAdmin):
	list_display=('name','district')

admin.ModelAdmin.search_fields=["uid","district","room_number","status"]

admin.site.register(Sale,SaleAdmin)
admin.site.register(Rent,RentAdmin)
admin.site.register(New_builds,NewAdmin)
admin.site.register(Users,UserAdmin)
admin.site.register(Admins,AdminsAdmin)
