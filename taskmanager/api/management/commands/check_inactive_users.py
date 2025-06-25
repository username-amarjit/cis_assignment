from django.core.management.base import BaseCommand
from api.models import Task, User
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Deactivate users with 5+ in progress and pending tasks in last 7 days'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(role='user', is_active=True)

        for user in users:
            missed_tasks = Task.objects.filter(
                assigned_to=user,
                status__in=['pending', 'inprogress'],
            ).count()
            self.stdout.write(f"Checking user: {user.username}, missed tasks: {missed_tasks}")
            if missed_tasks >= 5:
                user.is_active = False
                user.save()
                self.stdout.write(f"Deactivated {user.username} for missing {missed_tasks} tasks.")
