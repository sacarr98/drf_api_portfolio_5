from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from exercise.urls import exercise_router

router = DefaultRouter()
router.registry.extend(exercise_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path("api/", include((router.urls, 'api'))),
    path('', include('profiles.urls')),
    path('', include('progress.urls')),
]