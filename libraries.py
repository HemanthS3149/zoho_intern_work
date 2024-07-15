#we try to make a HTTP GET request to fetch data from an API

import requests

def fetch_data(url):
    try:
        response=requests.get(url)
        response.raise_for_status() #we ensure we process only successfull operations from the server
        return response.json()#for human readability, converts HTTP response into a python dictionary or lis
    
    except requests.exceptions.HTTPError as http_err: #http server fails to get processes
        print(f"HTTP error occurred:{http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

data=fetch_data("https://api.github.com")
print(data)
