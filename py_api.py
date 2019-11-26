import requests
r = requests.get('https://data.heroku.com/dataclips/qhsrzhbxankazauihhmaacloijyp.json?access-token=3420cf85-099d-4550-9c6a-3919ba79cc7a')
print r.text
