from django.utils import timezone
from .models import Task, Attendance
from sklearn.cluster import KMeans
import numpy as np

def get_productivity_insights(user):
    tasks = Task.objects.filter(employee=user, completed=True)
    if not tasks:
        return ["Complete more tasks to receive productivity insights."]

    completion_times = []
    hours = []
    for task in tasks:
        if task.completion_time and task.assigned_date:
            duration = (task.completion_time - task.assigned_date).total_seconds() / 3600
            hour = task.completion_time.hour
            completion_times.append([duration])
            hours.append([hour])

    if not completion_times:
        return ["No completion data available yet."]

    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(completion_times)
    labels = kmeans.labels_

    insights = []
    if len(set(labels)) > 1:
        fast_cluster = min(kmeans.cluster_centers_)
        if fast_cluster[0] < 24:
            insights.append("You complete tasks faster when assigned early in the day.")
    else:
        insights.append("Try completing tasks at different times to identify peak productivity.")

    return insights