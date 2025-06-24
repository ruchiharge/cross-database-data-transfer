import json 

def transformUserData(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        jsonData = json.load(f) 

    transformedData = {"entity": []} 
    for obj in jsonData:
        transformedObj = {
            "userId": obj["userId"],
            "userName": obj["userName"],
            "currProjects": obj["currProjects"],
            "finishedProjects": obj["finishedProjects"],
            "rating": obj["rating"]
        }
        transformedData["entity"].append(transformedObj)

    with open(outputFile, 'w') as f:
        json.dump(transformedData, f, indent = 4)

def transformProjectData(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        jsonData = json.load(f) 

    transformedData = {"entity": []} 
    for obj in jsonData:
        transformedObj = {
            "projectId": obj["projectId"],
            "projectName": obj["projectName"],
            "version": obj["version"],
            "startDate": obj["startDate"],
            "status": obj["status"]
        }
        transformedData["entity"].append(transformedObj)

    with open(outputFile, 'w') as f:
        json.dump(transformedData, f, indent = 4)

def transformCollaborationData(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        jsonData = json.load(f) 

    transformedData = {"entity": []} 
    for obj in jsonData:
        transformedObj = {
            "projectId": obj["projectId"],
            "userId": obj["userId"]
        }
        transformedData["entity"].append(transformedObj)

    with open(outputFile, 'w') as f:
        json.dump(transformedData, f, indent = 4)

userInput = 'userData.json'
projectInput = 'projectData.json'
collaborationInput = 'collaborationData.json'

transformUserData(userInput, userInput) 
transformProjectData(projectInput, projectInput) 
transformCollaborationData(collaborationInput, collaborationInput) 
print(f"Transformed data saved to '{userInput}', '{projectInput}' and '{collaborationInput}'") 
