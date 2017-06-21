from banglaidj import celery_app
from time import sleep

@celery_app.task()
def UploadTask(message):
    UploadTask.update_state(state="PROGRESS", meta={'progress':0})
    sleep(30)
    UploadTask.update_state(state="PROGRESS", meta={'progress':0})

    return message

def get_task_status(task_id):
    task = UploadTask.AsyncResult(task_id)

    status = task.status
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = task.info['progress']

    return {'status':status, 'progress':progress}
