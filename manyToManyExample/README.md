# Collaboration Portal

## Gilhari_CollabHub_AWS 

This example describes a many-to-many relationship between Users and Projects.

User details include `userId`, `userName`, `currProjects`, `finishedProjects` and `rating`. `id` is the primary key.

Project details include `projectId`, `projectName`, `version`, `startDate` and `status`. `id` is the primary key.

The `collaboration` table stores the mapping of userId to projectId. 

A user can have multiple projects. Many users can work on same project.

To add other constraints, you would have to mention them in the `.jdx` file in `config` directory.

## python_src

`dataDenerator.py` will generate dummy data for testing and store them in `userData.json`, `projectData`, `collaborationData.json`.

`transformData.py` will transform the generated data into the format required for sending the data through POST API call.

You can then make API calls by running `apiCall.py`.