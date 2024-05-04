

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_like_notification_email(author_email, recipe_title, like_count):
    subject = f'Your recipe "{recipe_title}" received {like_count} likes!'
    message = f'Congratulations! Your recipe "{recipe_title}" received {like_count} likes.'
    recipient_list = [author_email]
    send_mail(subject, message, 'puneet.jsr02@gmail.com', recipient_list)
