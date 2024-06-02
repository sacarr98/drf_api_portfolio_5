from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exercise.urls import exercise_router_router
from user.views import UserViewSet

router = DefaultRouter()
router.registry.extend(exercise_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include((router.urls, 'api'))),
    path('', include('profiles.urls')),
]
