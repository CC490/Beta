"""my_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import include
from django.views.generic.base import TemplateView
from reservation import views
from homepage.views import HomeReservationView
#from reservation import views as reservation_views
from status import views as status_views

urlpatterns = [

    path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('', views.HomeReservationView, name='home'),
	path('', HomeReservationView, name='home'),

#  new in beta_1

   path('reservation/', include('reservation.urls')),
   path('reports/', include('reports.urls')),

# new in beta3
   path('status/', include('status.urls')),



#   path('reviseReservation/<int:id>/', reservation_views.ReviseReservationView, name='Edit Reservation'),

# end new

#    path('reviseReservation/', reservation_views.ReviseReservationView, name='Revise Reservation'),
#    path('reservationSummary/', reservation_views.ReservationSummaryView, name='Reservation Summary'),
#    path('reviseReservation/reservationSubmit/', reservation_views.ReviseReservationRedView, name = 'Reservation Submitting'),
#    path('status/<int:id>', status_views.ReviseStatusView, name='Reservation Status'),
#    path('statusSummary/<int:id>', status_views.StatusSummaryView, name='Status Summary'),
    #path('status/<int:pk>', status_views.StatusView.as_view(), name='Reservation Status'),
    #path('reports/', TemplateView.as_view(template_name='reports.html'), name='reports'),
]
