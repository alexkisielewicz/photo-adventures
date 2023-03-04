from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
if os.path.isfile('env.py'):
    import env


@receiver(post_save, sender=User)
def send_new_user_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New user registered!'
        message = f'A new user {instance.username} has registered'
        from_email = os.environ.get('FROM_EMAIL')
        recipient_list = ["os.environ.get('RECIPIENT_LIST')"]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
