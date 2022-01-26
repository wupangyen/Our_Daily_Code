# import requests library
from urllib.request import HTTPBasicAuthHandler
from argon2 import extract_parameters
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


# How to Handle HTTP Errors with Python Requests
# The Basics of HTTP Status Codes

# 5 categories
# 1xx Informational - Indicates that a request has been received and that the client should continue to make the 
# requests for the data payload
# 2xx Successful - Indicates that a requested action has been received, understood, and accepted. 
# 3xx Redirection - Indicates that the client must take an additional action to complete the request like accessing the resource via a proxy or a
# different endpoint
# 4xx Client Error - Indicates problems with the client, such as a lack of authorization, forbidden access, disallowed methods, or attempts
# to access nonexistent resources.
# 5xx Server Error - Indicates problems with the server that provides the API. THere are a large variety of server
# errors and they often require the API provider to resolve


# How to Check for HTTP Errors with Python Requests

# the response objects has a status_code attribute that can be used to check for any errors the API might have reported

# Example Below shows how to use this attribute to check for successful and 404 not found HTTP status codes 

response9 = requests.get("http://api.open-notify.org/astros.json")
if(response9.status_code == 200):
    # Code here will only run if the request is successful
    print("The request was a success!")
elif(response9.status_code == 404):
    # Code here will react to failed requests
    print("Result not found!")
    
# Here is another way to Check for HTTP Errors with Python Requests
# requests to raise an exception for all error codes(4xx and 5xx), you can use the raise_for_status() function and
# catch specific errors using Requests built-in exceptions

try:
    response10 = requests.get('http://api.open-notify.org/astros.json')
    status = response10.raise_for_status()
    print(status)
    # will run if the request is successful

except requests.exceptions.HTTPError as error:
    print(error)
    # run if there is a 404 error


#Too Many Redirects 
# indicated by 3xx HTTP status codes is the requirement to redirect to a different location for the resource you're requesting
# can sometimes result in a situation where you end up with an infinite redirect loop
# The Python Requests module has the TooManyRedirects error that you can use to handle this problem.
# To resolve this problem, it's likely the URL you're using to access the resource is wrong and needs to be changed


# you can optionally use the request options to set the maximum number of redirects:
try:
    session1 = requests.Session()
    session1.max_redirects = 3
    response11 = session1.get('http://api.open-notify.org/astros.json')
   
    status = response11.raise_for_status()
    print(status)
    # will run if the request is successful

except requests.exceptions.HTTPError as error:
    print(error)
    # run if there is a 404 error


# or disable redirecting completely within your request options:
response12 = requests.get("http://api.open-notify.org/astros.json", allow_redirects=False)
if(response12.status_code == 200):
    # Code here will only run if the request is successful
    print("The request was a success!")
elif(response12.status_code == 404):
    # Code here will react to failed requests
    print("Result not found!")



#Connection Error
# What happens if you don't receive a response from the server at all
# Connection errors can occur for many different reasons, including a DNS failure, refused connection, internet
# connectivity issues or latency somewhere in the network

try:
    response13 = requests.get('http://api.open-notify.org/astros.json')
    status = response13.raise_for_status()
    print(status)
    # will run if the request is successful

except requests.ConnectionError as error:
    print(error)
    # run if there is a 404 error

#Timeout
#Timeout errors when you're able to connect to the API server, but it doesn't complete the request within the
#allotted amount of time
# In this example, the timeout was set as a fraction of a second via the request options. Most APIs are unable to
# respond this quickly

try:
    response14 = requests.get('http://api.open-notify.org/astros.json',  timeout=0.00001)
    status = response14.raise_for_status()
    print(status)
except requests.Timeout as error:
    print(error)

# How to Make Robust API Requests
# if we put all of the errors we've talked about together, we have a rather seamless way to handle any HTTP request
#error that comes our way

try:
    response15 = requests.get('http://api.open-notify.org/astros.json', timeout = 5)
    status = response15.raise_for_status()
    print(status)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
