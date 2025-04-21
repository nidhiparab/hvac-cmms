from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'tasks', views.MaintenanceTaskViewSet)
router.register(r'logs', views.MaintenanceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard-summary/', views.dashboard_summary, name='dashboard-summary'),
]