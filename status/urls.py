from django.urls import path, include, reverse
from . import views

urlpatterns = [

    path('statusSummary/<int:id>/', views.StatusSummaryView, name='Status Summary'),
    path('editStatus/<int:id>/', views.ReviseStatusView, name='Edit Status'),
    path('deleteStatus/<int:id>/', views.DeleteStatusView, name='Delete Status'),
    path('editStatus/<int:id>/statusUpdate/', views.ReviseStatusRedView, name='Status Updating'),
    path('pdf/<int:id>/', views.StatusPDFView, name='Status PDF'),

]