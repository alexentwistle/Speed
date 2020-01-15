# Get URL from user input, and append to Google PageSpeedInsights API URL, and curl (or equivalent). 
# This will use the requests library for convenience.

import requests
import json

url = input("What URL would you like to check: ")

params = (
    ('url', url),
)

response = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed', params=params)

json_string = response.json()
print(json_string)



with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_string, f, ensure_ascii=False, indent=4)