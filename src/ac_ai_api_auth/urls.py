from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views
app_name = "ac_ai_api_auth"

urlpatterns = [
    # remove these if you decide not to use GUI
    path('login/',
          LoginView.as_view(redirect_authenticated_user=True,
                            template_name="ac_ai_api_auth/login.html"),
                            name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # TODO: decide if we keep this view or not
    path('get_token_auth_api/', rest_views.obtain_auth_token, name='generate_token_api_view'),
    path('get_token_auth/', views.generate_token_view, name='generate_token'),
]
