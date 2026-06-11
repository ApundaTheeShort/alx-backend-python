import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'

    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(
        max_length=100, blank=False, null=False, unique=True, db_index=True)
    password_hash = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(choices=RoleChoices.choices,
                            default=RoleChoices.GUEST, max_length=15, null=False, blank=False)
    # created_at = models.DateTimeField(default=timezone.now, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name}, {self.last_name} {self.role}"


class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sender_id} sent {self.message_body} at {self.sent_at}"


class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    participants_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Conversation between {self.participants_id} created at {self.created_at}"
