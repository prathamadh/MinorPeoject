import requests

# URL of the server
url = 'http://192.168.11.104:5000/api'

# Data to be sent in the POST request
data = {'st': 'pratham adhikari'}

# Send POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("POST Request Successful")
else:
    print("POST Request Failed")

# Send GET request to retrieve the stored string
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     print("GET Request Successful")
#     print("Stored string:", response.text)
# else:
#     print("GET Request Failed")
