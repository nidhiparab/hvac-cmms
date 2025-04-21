from django.contrib import admin
from .models import Equipment, MaintenanceTask, MaintenanceLog

# Optional: Customize admin display
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'installation_date', 'last_service_date')
    search_fields = ('name', 'location')

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'task_type', 'frequency', 'last_performed', 'next_due_date')
    list_filter = ('task_type', 'frequency')
    search_fields = ('equipment__name',)

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'technician_name', 'completion_date', 'status')
    list_filter = ('status',)
    search_fields = ('technician_name', 'task__equipment__name')
