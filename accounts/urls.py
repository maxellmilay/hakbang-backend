from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView, UserProfileView, LogoutView, OrganizationView, UsernameAndEmailCheckerView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('organizations/', OrganizationView.as_view({'get': 'list', 'post': 'create'}), name='organizations'),
    path('organizations/<int:pk>/', OrganizationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='organization'),
    path('username-and-email-checker/', UsernameAndEmailCheckerView.as_view({'get': 'list'}), name='username_and_email_checker'),
]