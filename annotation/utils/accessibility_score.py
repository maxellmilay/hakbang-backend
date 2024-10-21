from celery import shared_task

@shared_task(bind=True)
def recalculate_scores(self, interval_in_seconds=5):
    print(f"Task executed with interval: {interval_in_seconds} seconds")

    """
    run `celery -A main worker --beat --loglevel=info`
    """
    
    # logic here
    print("Task is running...")

    # Reschedule the task to run again after the specified interval
    self.apply_async(args=[interval_in_seconds], countdown=interval_in_seconds)
    return "hi btich"
