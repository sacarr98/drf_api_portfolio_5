from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise, WorkoutExerciseDetail

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

    def create(self, validated_data):
        request_user = self.context['request'].user
        instance = Exercise.objects.create(user=request_user, **validated_data)
        return instance


class WorkoutExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExerciseDetail
        fields = ['id', 'sets', 'reps', 'weight']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='exercise.name', read_only=True)
    workout_exercise_details = WorkoutExerciseDetailSerializer(many=True, required=False)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise', 'name', 'workout_exercise_details']


class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True, required=False)

    class Meta:
        model = Workout
        fields = ['id', 'status', 'created', 'modified', 'workout_exercises']

    def create(self, validated_data):
        """Writable Nested Model Serializer"""
        request_user = self.context['request'].user
        instance = Workout.objects.create(user=request_user, status=validated_data.pop('status'))

        if 'workout_exercises' in validated_data:
            for data in validated_data.pop('workout_exercises'):
                exercise = data.get('exercise')
                workout_exercise = WorkoutExercise.objects.create(workout=instance, exercise=exercise)

                if 'workout_exercise_details' in data:
                    for exercise_details in data.get('workout_exercise_details'):
                        WorkoutExerciseDetail.objects.create(workout_exercise=workout_exercise, **exercise_details)

        return instance