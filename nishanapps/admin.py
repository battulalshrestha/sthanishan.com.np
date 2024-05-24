from django.contrib import admin
from .models import Patient
admin.site.site_header = "Nishan pvt ltd"
admin.site.index_title = "Nishan ko index"
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','oda_number','email','password')
# Register your models here.



#cd nishanproject
#python3 manage.py runserver