from django.db import models
from authapi.models import User

# Create your models here.

MAX_CODE_LENGTH = 10

class Verifier(models.Model):
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_to')
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_from')
    verification_code = models.CharField(max_length=MAX_CODE_LENGTH)
    time_sent = models.DateTimeField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




