from django.urls import path, include, reverse
from . import views

urlpatterns = [

   # need to look at new vs revise redirect views, reservationSubmit/
   path('', views.NewReservationView, name='New Reservation'),
   path('reservationCreate/', views.NewReservationRedView, name='Creating Reservation'),
   path('reviseReservation/<int:id>/', views.ReviseReservationView, name='Revise Reservation'),
   path('reservationSummary/<int:id>', views.ReservationSummaryView, name='Reservation Summary'),
    path('deleteReservation/<int:id>/', views.DeleteReservationView, name='Delete Reservation'),

# this one we can do url reversing on if we (A) make homepage urls, (B) make them have namespace    
   path('reviseReservation/<int:id>/reservationSubmit/', views.EditReservationRedView, name = 'Reservation Updating'),

#   path('^/$', views.HomeReservationView, name='Home'),
]