from celery import shared_task
from .models import Event

@shared_task
def cleanup():
    # res = Event.objects.filter().order_by('-id')[0]
    print('clean up the Trash')
    # print(res.datetime)


