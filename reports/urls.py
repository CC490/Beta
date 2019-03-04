from django.urls import path, include, reverse
from . import views

urlpatterns = [

   # need to look at new vs revise redirect views, reservationSubmit/
   path('', views.ReportView, name='Reports'),
   path('monthVis/', views.MonthVisView, name='Month Visitors'),
   path('attRep/', views.AttendView, name='Attendance Report'),
   path('acctRec/', views.AcctRecView, name='Accounts Receivable'),
   path('allData/', views.AllDataView, name='All Data'),
]