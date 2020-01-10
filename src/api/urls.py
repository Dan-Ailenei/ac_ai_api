from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('result/', views.NlpResultView.as_view(), name='result'),
]
