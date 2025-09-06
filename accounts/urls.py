from django.urls import path, include
from .views import clientRegisterView, ArchitectRegisterView, LoginView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/clients/', clientRegisterView.as_view(), name='register-client'),
    path('register/architects/', ArchitectRegisterView.as_view(), name='register-architect/'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('myprofile/', ProfileView.as_view(), name='myprofile'),
]
