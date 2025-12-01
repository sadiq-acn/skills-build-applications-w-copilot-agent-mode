
from django.test import TestCase
from .models import UserProfile, ActivityLog, Team, Leaderboard, Workout

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Marvel")
    def test_team(self):
        team = Team.objects.get(name="Marvel")
        self.assertEqual(team.name, "Marvel")

class UserProfileTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Alpha")
        UserProfile.objects.create(username="testuser", email="test@example.com", team=team)
    def test_user_profile(self):
        user = UserProfile.objects.get(username="testuser")
        self.assertEqual(user.email, "test@example.com")

class ActivityLogTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Beta")
        user = UserProfile.objects.create(username="testuser2", email="test2@example.com", team=team)
        ActivityLog.objects.create(user=user, activity_type="Running", duration=30, calories_burned=300, date="2025-12-01")
    def test_activity_log(self):
        activity = ActivityLog.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, 30)

class WorkoutTestCase(TestCase):
    def setUp(self):
        Workout.objects.create(name="Full Body Blast", description="A superhero workout for all muscles.")
    def test_workout(self):
        workout = Workout.objects.get(name="Full Body Blast")
        self.assertEqual(workout.description, "A superhero workout for all muscles.")

class LeaderboardTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Gamma")
        user = UserProfile.objects.create(username="testuser3", email="test3@example.com", team=team)
        Leaderboard.objects.create(user=user, points=150)
    def test_leaderboard(self):
        entry = Leaderboard.objects.get(points=150)
        self.assertEqual(entry.user.username, "testuser3")
