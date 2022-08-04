import os
import requests
from celery.schedules import crontab
from django.core.cache import cache
from gozagel.celery import app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gozagel.settings")


@app.task
def get_exchange_rates():
    try:
        res = requests.get(
            "http://data.fixer.io/api/latest",
            params={
                "access_key": "100f2c93d2ca082c20b01fa1ed4b5794",
                "symbols": "USD, EGP, GBP",
            },
        )
        response = res.json()
        rates = response["rates"]
        for curr, rate in rates.items():
            cache.set(curr, str(rate), timeout=None)

    except:
        print("task cannot run")


app.conf.beat_schedule = {
    "get-rates-every-6-hours": {
        "task": "rates.tasks.get_exchange_rates",
        "schedule": crontab(minute="*/2"),
    },
}
