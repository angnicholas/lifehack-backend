from django.urls import include, path
from .views import CustomTokenObtainPairView, CustomUserCreateView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('jwt/login', CustomTokenObtainPairView.as_view()),
    path('register', CustomUserCreateView.as_view()),
]

# from rest_framework import routers

# from .views import RegisterView, LoginView, UserView, LogoutView

# urlpatterns = [
# 	path('login', LoginView.as_view()),
# 	path('user', UserView.as_view()),
# 	path('logout', LogoutView.as_view()),
# 	path('register', RegisterView.as_view())
# ]
