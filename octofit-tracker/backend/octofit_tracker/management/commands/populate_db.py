from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date='2026-02-05'),
            Activity(user='Captain America', type='swim', duration=45, date='2026-02-04'),
            Activity(user='Batman', type='cycle', duration=60, date='2026-02-03'),
            Activity(user='Wonder Woman', type='yoga', duration=50, date='2026-02-02'),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=110)

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Sprints', description='Run 5 sprints', difficulty='medium'),
            Workout(name='Deadlift', description='Deadlift 100kg', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
