from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(APITestCase):
    def test_list_teams(self):
        url = reverse('team-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(APITestCase):
    def test_list_activities(self):
        url = reverse('activity-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTests(APITestCase):
    def test_list_leaderboard(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(APITestCase):
    def test_list_workouts(self):
        url = reverse('workout-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
