import requests
import json
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=30)
searchDate = datetime.today() - timeBefore

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(searchDate.timestamp()),
    "tagged": "python",
    "min": 15
}
r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()

except json.decoder.JSONDecodeError:
    print("incorrect format")

else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
