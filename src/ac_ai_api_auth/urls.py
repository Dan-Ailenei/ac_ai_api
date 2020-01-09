from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "ac_ai_api_auth"

urlpatterns = [
    path('login/',
          LoginView.as_view(redirect_authenticated_user=True,
                           template_name="ac_ai_api_auth/login.html"),
          name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
