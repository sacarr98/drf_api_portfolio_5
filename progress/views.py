from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from project_api.permissions import IsOwnerOrReadOnly
from .models import Weight
from .serializers import WeightSerializer


class WeightList(generics.ListCreateAPIView):
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Weight.objects.order_by('-updated_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
