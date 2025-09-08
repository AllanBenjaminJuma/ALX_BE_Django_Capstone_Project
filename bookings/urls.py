from django.urls import path
from .views import ClientBookingListCreateView, BookingDetailView, ArchitectBookingListView

urlpatterns = [
    path('clients/bookings/', ClientBookingListCreateView.as_view(), name='client-bookings'),
    path('bookings/<int:pk>/', BookingDetailView().as_view(), name='booking-details'),
    path('architects/bookings/', ArchitectBookingListView().as_view(), name='architect-bookings')
]
