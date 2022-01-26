"""
Goal is to list the most active authors 

list of users  with submission count greater than threshold


"""
import requests
# Here is the url
#https://jsonmock.hackerrank.com/api/article_users?page=1

def most_activate_authors(threshold):
    # set variables
    # 1. result list
    # 2. current page 
    # 3. total page

    res = []
    currentPage = 1
    totalPage = 0

    response = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=1')

    totalPage = response.json()["total_pages"]
    # need a way to loop through each page
    while currentPage <= totalPage:
        response1 = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=' + str(currentPage))
        data = response1.json()['data']
        print(data)
        
        # loop though each data to find value for submission_count
        for d in data:
            submission_count = d['submission_count']
            print(submission_count)
            username = d['username']
            print(username)
            # check if the submission count > threshold, if it is add the username to the result list 
            if(submission_count > threshold):
                res.append(username)
            
        # increment current page
        currentPage += 1
    #return res
    return res
    print(totalPage)

authors = most_activate_authors(10)
print(authors)
