from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Equipment, MaintenanceTask, MaintenanceLog
from .serializers import EquipmentSerializer, MaintenanceTaskSerializer, MaintenanceLogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from datetime import datetime, timedelta

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class MaintenanceTaskViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTask.objects.all()
    serializer_class = MaintenanceTaskSerializer

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    
@api_view(['GET'])
def dashboard_summary(request):
    # Get counts for dashboard
    equipment_count = Equipment.objects.count()
    
    # Tasks due this week
    one_week_from_now = datetime.now().date() + timedelta(days=7)
    tasks_due_soon = MaintenanceTask.objects.filter(next_due_date__lte=one_week_from_now).count()
    
    # Tasks by status
    tasks_completed = MaintenanceLog.objects.filter(status='completed').count()
    tasks_with_issues = MaintenanceLog.objects.filter(status='issue_found').count()
    
    return Response({
        'equipment_count': equipment_count,
        'tasks_due_soon': tasks_due_soon,
        'tasks_completed': tasks_completed,
        'tasks_with_issues': tasks_with_issues
    })

# Create your views here.
