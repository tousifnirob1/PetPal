from django.contrib import admin
from .models import Pet, CareGiver, VetAppointment

admin.site.register(Pet)
admin.site.register(CareGiver)

@admin.register(VetAppointment)
class VetAppointmentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'pet_name', 'date', 'time', 'vet_name', 'is_confirmed')  
    list_filter = ('date', 'is_confirmed') 
    search_fields = ('user_name', 'pet_name', 'vet_name')  