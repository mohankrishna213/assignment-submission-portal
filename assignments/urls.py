from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_assignment, name='upload_assignment'),
    path('assignments/', views.view_assignments, name='view_assignments'),
    path('assignments/<int:assignment_id>/<str:action>/', views.manage_assignment, name='manage_assignment'),
]
