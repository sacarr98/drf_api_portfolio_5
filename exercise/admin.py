from django.contrib import admin

from .models import Exercise, Workout, WorkoutExercise, WorkoutExerciseDetail


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_part', 'name', 'equipment', 'description', 'user')


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created', 'modified')


class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout', 'exercise')


class WorkoutExerciseDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_exercise', 'sets', 'reps', 'weight')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
admin.site.register(WorkoutExerciseDetail, WorkoutExerciseDetailAdmin)