#from django.urls import path
#from exercise import views

#urlpatterns = [
#    path('exercises/', views.ExerciseViewSet.as_view()),
#    path('workouts/', views.WorkoutViewSet.as_view()),
#]

from rest_framework.routers import SimpleRouter

from .views import ExerciseViewSet, WorkoutViewSet

exercise_router = SimpleRouter()

exercise_router.register(r'exercise', ExerciseViewSet, basename='exercise')
exercise_router.register(r'workout', WorkoutViewSet, basename='workout')