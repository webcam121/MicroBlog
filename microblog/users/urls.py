from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

from .views import EmailTokenObtainPairView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
]