import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "VCNf6g9u_HfAeP05pKqcLrkRfqL05pVaGhGJxh1XA47jvFFe3megA3laCisE3fFrNLGyMD4mTQFh-vdq862NiD9jgA48n5fxzCuEnCM9ES0H_GIprvirHqoMrIByXXYx"
headers = {
    "Authorization": "Bearer "+api_key
}
params = {
    "location":"Montreal",
    "term":"cafe"
}
response = requests.get(url=url, headers=headers, params=params)
results = response.json()["businesses"]
names = [business["name"] for business in results if business["rating"] > 4.0]
for name in names:
    print(name)