
from django.contrib import admin
from .models import UserProfile, ActivityLog, Team, Leaderboard, Workout

admin.site.register(UserProfile)
admin.site.register(ActivityLog)
admin.site.register(Team)
admin.site.register(Leaderboard)
admin.site.register(Workout)
