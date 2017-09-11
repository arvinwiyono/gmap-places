import requests
import json
import pandas as pd
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
key = "change_this"
cities = [
    'jakarta',
    'surabaya',
    'malang',
    'semarang'
]
cols = ['street_address', 'lat', 'long']
df = pd.DataFrame(columns=cols)

for city in cities:
    querystring = {"query":f"indomaret in {city}","key":key}
    res = requests.request("GET", url, params=querystring)
    json_res = json.loads(res.text)
    for result in json_res['results']:
        address = result['formatted_address']
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        df = df.append(pd.Series([address, lat, lng], index=cols), ignore_index=True)
df.to_csv('for_pepe.csv', index=False)
