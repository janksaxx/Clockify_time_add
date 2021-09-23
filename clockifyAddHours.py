import datetime
from datetime import date
import requests



today = date.today()
d1 = today.strftime("%Y-%m-%d")

    

    # validate API variables


    # set clockify api URL
url = f"https://api.clockify.me/api/workspaces/{ClockifyWorkspaceID}/timeEntries"

# build payload
# start_dt is set to noon else clockify might set it the day before.
start_dt = datetime.datetime.combine(
    datetime.date.fromisoformat(d1), datetime.time(hour=8)
)
end_dt = start_dt + datetime.timedelta(hours=8.0)

fmt = "%Y-%m-%dT%H:%M:%SZ"
data = {
    "start": start_dt.strftime(fmt),
    "end": end_dt.strftime(fmt), 
    "billable": "true",
  "description": "Working",
  "projectId": {ClockifyProjectID}
}

# post payload
r = requests.post(url, json=data, headers={"X-Api-Key": {UserAPIKeyForWhichTimeIsToBeAdded}})




