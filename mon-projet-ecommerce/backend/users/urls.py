from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, LogoutView, ProfileView, CookieTokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('refresh/', CookieTokenRefreshView.as_view(), name='refresh'), 
]