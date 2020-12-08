import requests 

def lambda_handler(event=None, context=None):
    r = requests.get("https://www.pylenin.com")
    if r.status_code == 200:
        return "It Was Successfull"