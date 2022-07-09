from django.core.management.base import BaseCommand
from authapi.models import User
from verifier.models import Verifier

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create(
            email='institution1@test.com',
            display_name='Institution 1',
            role='IN', 
            password='pbkdf2_sha256$320000$fzVxGO5DcNsQhOG3XMXUas$f/pSnQxfGi1Ld5ij+0DhyVFZDJIP6Ui/ZvomRLIYZok='
        )

        User.objects.create(
            email='user1@test.com',
            display_name='User 1',
            role='EU', 
            password='pbkdf2_sha256$320000$fzVxGO5DcNsQhOG3XMXUas$f/pSnQxfGi1Ld5ij+0DhyVFZDJIP6Ui/ZvomRLIYZok='
        )