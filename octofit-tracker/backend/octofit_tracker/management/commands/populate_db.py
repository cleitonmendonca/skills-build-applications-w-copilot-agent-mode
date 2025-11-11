from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.apps import apps

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince'),
        ]

        # Create activities
        Activity.objects.create(name='Flight', user='ironman', team='Marvel')
        Activity.objects.create(name='Shield Throw', user='captainamerica', team='Marvel')
        Activity.objects.create(name='Martial Arts', user='batman', team='DC')
        Activity.objects.create(name='Lasso', user='wonderwoman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='captainamerica', team='Marvel', score=90)
        Leaderboard.objects.create(user='batman', team='DC', score=95)
        Leaderboard.objects.create(user='wonderwoman', team='DC', score=98)

        # Create workouts
        Workout.objects.create(name='Arm Day', description='Bicep curls and triceps extensions', user='ironman')
        Workout.objects.create(name='Shield Training', description='Shield throws and defense', user='captainamerica')
        Workout.objects.create(name='Stealth', description='Night training and gadgets', user='batman')
        Workout.objects.create(name='Amazonian Strength', description='Strength and agility', user='wonderwoman')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
