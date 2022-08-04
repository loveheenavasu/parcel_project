from celery import Celery

app = Celery("tasks")
app.config_from_object("gozagel.celeryconfig")
app.autodiscover_tasks()
