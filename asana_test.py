import os
import asana
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

def get_completed():

    current_time_utc = datetime.utcnow()

    adjusted_time_utc = current_time_utc - timedelta(minutes=3)

    # Format the adjusted time as a string in the required asana format
    adjusted_timestamp = adjusted_time_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    # Asana client
    client = asana.Client.access_token(os.getenv('ASANA_ACCESS_TOKEN'))

    result = client.tasks.get_tasks(
        {
        'project':os.getenv('ASANA_PROJECT_GID'),
        'modified_since': adjusted_timestamp
        }, 
        opt_pretty=True, 
        opt_fields=['name','completed']
        )


    return result