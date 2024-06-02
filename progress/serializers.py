from rest_framework import serializers
from progress.models import Weight

class WeightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    goal_weight = serializers.ReadOnlyField(source='owner.profile.goal_weight')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Weight
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 
            'updated_at', 'goal_weight', 'current_weight',
        ]