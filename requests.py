import json
import requests
from requests.exceptions import HTTPError


jokes_url ="https://icanhazdadjoke.com/"
details_url = "https://jsonplaceholder.typicode.com/users"

jokes_res = requests.request("GET", jokes_url,
                    headers={'Accept': 'application/json'}
                        )
 
jokes_api_res = jokes_res.json()

print(jokes_api_res)
print(jokes_res.headers['Content-Type']) #Checking the response type
print(jokes_res.status_code) # Checking the status codes
print(jokes_res.encoding)

details_res = requests.request("GET" ,details_url)
detail_api_res = details_res.json()
print(detail_api_res)


# Shorter alternative

for url in [details_url, jokes_url]:
    try:
        response = requests.request("GET" ,url,
                     headers={'Accept': 'application/json'}
                         )

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print(response.json())



