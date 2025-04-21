from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    installation_date = models.DateField()
    last_service_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class MaintenanceTask(models.Model):
    TASK_TYPES = [
        ('filter_change', 'Filter Change'),
        ('coil_cleaning', 'Coil Cleaning'),
        ('refrigerant_check', 'Refrigerant Check'),
        ('thermostat_calibration', 'Thermostat Calibration'),
        ('ductwork_inspection', 'Ductwork Inspection'),
    ]
    
    FREQUENCIES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annual', 'Annual'),
    ]
    
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    frequency = models.CharField(max_length=20, choices=FREQUENCIES)
    last_performed = models.DateField(null=True, blank=True)
    next_due_date = models.DateField()
    
    def __str__(self):
        return f"{self.get_task_type_display()} for {self.equipment.name}"

class MaintenanceLog(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('issue_found', 'Issue Found'),
    ]
    
    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE)
    technician_name = models.CharField(max_length=100)
    completion_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='maintenance_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.task} - {self.completion_date}"