from django.db import models
from log_reg_app.models import User

class MessageManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['message']) < 5:
            errors['message'] = "Message has to be at least 5 characters"
        return errors

class Message(models.Model):
    message = models.TextField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')