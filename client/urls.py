from django.urls import path
from .views import ClientProfileView

urlpatterns = [
    path('myprofile/', ClientProfileView.as_view(), name='client_profile'),
]
