import json 
import random 
import time
import datetime 
from faker import Faker 

fake = Faker() 

# function for generating single record
def generateUserRecord(userId):
    userId = userId
    userName = fake.name()
    currProjects = random.randint(0, 5)
    finishedProjects = random.randint(0, 20)
    rating = random.randint(1, 5)
    
    return {
        'userId': userId,
        'userName': userName,
        'currProjects': currProjects,
        'finishedProjects': finishedProjects,
        'rating': rating
    }

def generateProjectRecord(projectId):
    projId = projectId
    projectName = fake.catch_phrase()
    version = f"{random.randint(0,10)}.{random.randint(0,10)}.{random.randint(0,10)}"

    # generating start date and converting it into miliseconds since January 1, 1970
    startDate = fake.date_this_decade(before_today = True, after_today = False) 
    startDate_datetime = datetime.datetime(startDate.year, startDate.month, startDate.day)
    startDate_milliseconds = int(time.mktime(startDate_datetime.timetuple()) * 1000)

    status = random.choice(["Not Started", "In Progress", "Completed", "On Hold", "Cancelled"])
    
    return {
        'projectId': projId,
        'projectName': projectName,
        'version': version,
        'startDate': startDate_milliseconds,
        'status': status
    }

# generate 50 records
users = [generateUserRecord(i) for i in range(1, 51)]
projects = [generateProjectRecord(i) for i in range(1, 71)]
collaborations = []

userIds = [user['userId'] for user in users]
projectIds = [project['projectId'] for project in projects]

for projectId in projectIds:
    groupSize = random.randint(1,3)
    for i in range(groupSize):
        randomUser = random.choice(userIds) 
        collaborations.append({'projectId': projectId, 'userId': randomUser}) 

# save to a JSON file
with open('userData.json', 'w') as json_file:
    json.dump(users, json_file, indent=4)

with open('projectData.json', 'w') as json_file:
    json.dump(projects, json_file, indent=4)

with open('collaborationData.json', 'w') as json_file:
    json.dump(collaborations, json_file, indent=4)

print("Data generated and saved to userData.json")
print("Data generated and saved to projectData.json")
print("Data generated and saved to collaborationData.json")
