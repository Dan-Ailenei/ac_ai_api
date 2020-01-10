from django.urls import path
from django.conf.urls import include
from . import views

app_name = "nlp"

urlpatterns = [
    path('result/', views.NlpResultView.as_view(), name='result'),
]
