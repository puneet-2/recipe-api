from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('recipe_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Define periodic tasks
app.conf.beat_schedule = {
    'send-daily-likes-notification': {
        'task': 'your_app.tasks.send_daily_likes_notification',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
}
