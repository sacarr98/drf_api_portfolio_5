from django.urls import path
from progress import views

urlpatterns = [
    path('progress/', views.WeightList.as_view()),
]