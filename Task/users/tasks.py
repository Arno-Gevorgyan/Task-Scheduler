from celery import shared_task


@shared_task
def cleanup():
    print("Cleaning up the trash")

