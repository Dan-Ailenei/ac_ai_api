from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from ac_ai_api_auth import views
from ac_ai_api_auth.views import ApiLoginView
from knox import views as knox_views

app_name = "ac_ai_api_auth"

urlpatterns = [
    # remove these if you decide not to use GUI
    path('login/',
          LoginView.as_view(redirect_authenticated_user=True,
                            template_name="ac_ai_api_auth/login.html"),
                            name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('generate_token/', views.generate_token_view, name='generate_token'),

    path('api/auth/login/', ApiLoginView.as_view(), name='knox_login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
