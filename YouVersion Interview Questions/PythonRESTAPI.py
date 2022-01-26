# import requests library
from urllib.request import HTTPBasicAuthHandler
import requests
from requests.auth import HTTPBasicAuth

# use GET method 
response = requests.get("http://api.open-notify.org/astros.json")
#response object contains all the data sent from the server in response to your GET request, including headers and the data payload
print(response)

# ways to get the content of the request
#response.content() # return the raw bytes of the data payload
#response.text() # return a string representation of the data payload
response.json() # This method is convient when the API returns JSON


#How to use Query Parameters - used to filter the data that an API returns, these are added as query parameters
# that are appended to the endpoint URL
# this is handled via the params argument, which accepts a dictionary object

# Example: when we use the Open Notify API to GET an estimate for when the ISS will fly over a specified point:
query = {'lat':'45','lon':'180'}
response1 = requests.get('http://api.open-notify.org/iss-pass.json',params=query)
print(response1.json())

# How to Create and Modify Data with POST and PUT
# you can use the data argument to add the associated data for PUT and POST method requests
response2 = requests.post('https://httpbin.org/post',data={'key':'value'})

#Update an existing resource
requests.put('https://httpbin.org/put',data = {'key':'value'})

print(response2.json())

# How to Access REST Headers
#retrieve metadata from the response via headers. 
# For example, to view the date of the response specify that with the `headers` property:
response4 = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=1')
print(response4.headers["date"])


#JSON Object Literals
# This is a JSON string '{"name":"John", "age":30, "car":null}'

# JSON object literal surrounded by curly braces {}, contains key/value pairs
#{"name":"John", "age":30, "car":null}

# How to extract a value from JSON in Python
# Answer: Values are extracted from a JSON object by indexing the object by a specific key.
# Example: value "Bob" in json_object = {"id": 20, "name": "Bob"} is extracted by json_object["name"].

response5 = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=1')


article_users = response5.json()["data"]
print(article_users)


# I look into how to Authenticate to a REST API
# The simplest way is to pass your username and password to the appropriate endpoint as HTTP Basic Auth; this is
# equivalent to typing your username and password into a website

response6 = requests.get(
    'https://api.github.com/user',
    auth = HTTPBasicAuth('username','password')
)
print(response6)

# the more secure method is to get an access token that acts as an equivalent to a username/password combination

# most common framework for API authentication is OAuth

# Once you have an access token, you can provide it as a bearer token in the request header:
# this is the most secure way to authenticate to a REST API with an access token:

my_headers ={'Authorization':'Bearer{access_token}'}
response7 = requests.get('http://httpbin.org/headers', headers=my_headers)

print(response7)
# few methods to authenticate to a REST API, digest, Kerberos, NTLM and AuthBase

# Use Sessions to Manage Access Tokens
#persist parameters that are needed for making multiple requests within a single session

session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response8 = session.get('https://httpbin.org/headers')
print(response8)
