from django.urls import path
from . import views
app_name = "nlp"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.NlpResultView.as_view(), name='result'),
]
