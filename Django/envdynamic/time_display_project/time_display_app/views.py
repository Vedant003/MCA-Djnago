from django.http import HttpResponse
from datetime import datetime, timedelta

def time_after_10_hours(request, hours):
    try:
        hours = int(hours)
    except ValueError:
        return HttpResponse("Invalid input. Please provide a valid integer.")

    current_time = datetime.now()
    time_after_10_hours = current_time + timedelta(hours=hours)

    return HttpResponse(f"Current Time: {current_time}<br>Time After {hours} Hours: {time_after_10_hours}")
