import requests 
import json 

user_url = 'http://localhost:80/gilhari/v1/user/'
project_url = 'http://localhost:80/gilhari/v1/project/'
collaboration_url = 'http://localhost:80/gilhari/v1/collaboration/'
stop_url = 'http://localhost:80/gilhari/v1/quit/now'


def get_call(url, filterKey=None, filterVal=None, deep=None, maxObjects=None):

    # update url as per query parameters
    if filterKey != None and filterVal != None:
        url += '?filter=' + str(filterKey) + '=' + str(filterVal)
    elif deep != None:
        url += '?deep=' + str(deep)
    elif maxObjects != None:
        url += '?maxObjects=' + str(maxObjects)

    try: 
        response = requests.get(url)

        if response.status_code == 200:
            print("Successfuly called GET API")
            print("GET Response data: ")
            print(response.json()) 

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 


def post_call(url, dataDump):
    try: 
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, json = dataDump, headers = headers)

        if response.status_code == 201:
            print("Successfully inserted values")

        else:
            print(f"Error: {response.status_code}") 

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 


get_call(user_url)
get_call(project_url)
get_call(collaboration_url)

with open('userData.json', 'r') as f:
    jsonData = json.load(f) 
post_call(user_url, jsonData)

with open('projectData.json', 'r') as f:
    jsonData = json.load(f) 
post_call(project_url, jsonData)

with open('collaborationData.json', 'r') as f:
    jsonData = json.load(f) 
post_call(collaboration_url, jsonData)

get_call(stop_url)