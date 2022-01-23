"""
Python Requests Module

Definition and Usage: The requests module allows you to send HTTP requests using Python
The HTTP request returns a Response Object with all the response data

Syntax:
requests.methodname(params)

Method                  Description
get(url,params,args)    Sends a GET request to the specified url

Example:
Make a request to a web page, and print the response text:

import requests
x= requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)

"""

import requests 
"""
JSON is a syntax for storing and exchanging data 
JSON is text, written with JavaScript object notation 

JSON in Python
a built-in package called json, which can be used to work with JSON data

Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads method 
The result will be a Python dictionary

#dictionary in python is associative array

Example:
Convert from JSON to Python:

import json
#some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

#parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method

Examples: Convert from Python to JSON

import json
# a Python object (dict):

x={
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Format the Result json.dumps() methods has parameters to make it easier to read the result 
json.dumps(x, indent = 4)

use separators parameter to change the default separator:
json.dumps(x,indent=4, separators=(".","="))


use sort_keys parameters to specify if the result should be sorted or not

json.dumps(x,indent=4,sort_keys=True)

"""

import json



def getUsernames(threshold):
    # set variables 

    """user name list"""
    usernames = []
    page = 1
    totalPages = 1

    """while loop to see we are on the page we have data on it"""
    while page <= totalPages:

        # make request for each page 
        """make a get request"""
        apiRequest = requests.get('https://jsonmock.hackerrank.com/api/article_users?page='+str(page))
        articles = apiRequest.json()['data']

        """if we at first page we want to find out the total pages we need to loop through"""
        """set total pages value """
        if page == 1:
            totalPages = apiRequest.json()['total_pages']

        # get data for each user
        for val in articles:
            submissionCount = val['submission_count']

            # check if submissionCOunt is Greater than threshold 
            if submissionCount > threshold:
                usernames.append(val['username'])
        """go to the next page"""
        page += 1
        
        
    # return usernames 
    return usernames




names = getUsernames(10)
print(names)
