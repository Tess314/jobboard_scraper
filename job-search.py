import requests
import json
from send_email import send_email

URL = "https://remoteok.io/api"
keys = ['company','position','tags','location','url']

wanted_tags = ["python", "c", "c#", "java"] #or whatever tags are relevant to you 

def get_jobs():
    resp = requests.get(URL)
    job_results = resp.json()

    jobs = []
    for job_res in job_results:
        job = {k: v for k, v in job_res.items() if k in keys}

        if job:
            tags = job.get('tags')
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted_tags):
                jobs.append(job)

    return jobs


if __name__ == '__main__':
    my_jobs = get_jobs()

    if my_jobs:
        message = "Subject: Remote Jobs!\n\n"
        message += "Found some cool remote jobs!\n\n"

        for job in my_jobs:
            message += f"{json.dumps(job)}\n\n"

        send_email(message)
