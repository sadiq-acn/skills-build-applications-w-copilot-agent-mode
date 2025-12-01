
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import (
    UserProfileViewSet, ActivityLogViewSet, TeamViewSet, LeaderboardViewSet, WorkoutViewSet
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityLogViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('userprofile-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activitylog-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
