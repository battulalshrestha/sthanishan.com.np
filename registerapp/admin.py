from django.contrib import admin

# Register your models here.
from .models import Registerkoclasshaita
admin.site.site_header = "Nishan pvt ltd2"
admin.site.index_title = "Nishan ko index2"
@admin.register(Registerkoclasshaita)
class RegisterkoclasshaitaAdmin(admin.ModelAdmin):
   list_display1 = ['id','username_rakha','email_rakha','password_rakha','password_thikcha']