# Gilhari_AWS

## Overview  
 
Gilhari, available in a Docker image, is configurable as per an application specific object and relational models. Gilhari makes it easy to interact with the database by exposing a REST interface. It provides APIs (POST, GET, PUT, DELETE) that let you perform CRUD (Create, Read, Update, and Delete) operations on your application specific JSON objects.It eliminates the need to write any code to handle the REST APIs or to access the database.


We have shown two scenerios to describe the use of Gilhari:

### **simpleExample:**  
This example illustrates a simple case of **HR management**, where employee details are stored in a relational database. This part of the project utilizes an object model consisting of Employee objects and demonstrates the use of the Gilhari microservice to exchange JSON data for a **simple** object model with a (local or AWS) database.

### **manyToManyExample:**  

The many-to-many example showcases a **collaboration portal** where multiple users collaborate on various projects, creating a many-to-many relationship between users and projects. This part of the project uses an object model that includes a many-to-many relationship between User and Project objects. It demonstrates the use of Gilhari microservice to manage the exchange of JSON data for a **complex** object model with a (local or AWS) database.
 
## Softwares, Services and Packages used 

To use Gilhari, please ensure you have installed the following: 

1. **Gilhari SDK:** (0.8.0b) for source codes and configuration guide
2. **Docker Desktop:** (version 26.1.1) for running Gilhari container  
3. **JDK:** (version 1.8) for compiling `.java` and `.jar` files
4. **Postman:** (v11.2.12) for testing Gilhari REST APIs on local database 
5. **MySQL:** (version 8) This project uses MySQL for creating and using database, but you can use any other Relational Database Management System
6. **JDBC driver for MySQL:** for establishing connection to MySQL database
7. **Amazon Web Servies:** to create and use a relation database on cloud
8. **requests:** (optional) python library for making REST API calls through python script
9. **faker:** (optional) python library for creating dummy data 

To work with Gilhari, you need to configure it for your application.

# Setup and configuration of Gilhari
You can install **Gilhari SDK** from [here](https://www.softwaretree.com/v1/products/gilhari/download-gilhari.php) and follow these steps to configure Gilhari framework for your application. 

## 1. Define and compile empty Java (container) class  

To use Gilhari, we first define empty Java (container) classes for each conceptual type of the JSON objects (domain model classes) used in our application.

In `src\com\mycompany\Gilhari_HR_AWS\model` we create a file `JSON_Employee.java`. Here, Employee is a conceptual name for a type of JSON object. For defining any new container class `X`, you just have to create an `X.java` file and change `JSON_Employee` to `X` at three places in the code (as shown in manyToManyExample).

JAR files shipped with Gilhari SDK in the `libs\` directory are necessary to compile the Java files we have created. So, we create a `lib` directory and add `jdxtools.jar`, `json-20160212.jar` and `jxclasses.jar` in it. 

Now we compile the classes using javac for JDX ORM to use them. Command for compiling single java file (simpleExample):
```cmd
javac -source 8 -target 8 -cp "lib/jxclasses.jar;lib/jdxtools.jar;lib/json-20160212.jar" -d bin src/com/mycompany/Gilhari_HR_AWS/model/JSON_Employee.java
```    

Command for compiling all java files simultaneously `(recommended)` (manyToManyExample): 
```cmd
javac -source 8 -target 8 -cp "lib/jxclasses.jar;lib/jdxtools.jar;lib/json-20160212.jar" -d bin src/com/mycompany/Gilhari_Collabhub_AWS/model/JSON_User.java src/com/mycompany/Gilhari_Collabhub_AWS/model/JSON_Project.java src/com/mycompany/Gilhari_CollabHub_AWS/model/JSON_Collaboration.java 
```

>Note: Use JDK 1.8 (Java 8) for compatibility with the Gilhari runtime, as Gilhari is designed to work with Java 8 features and bytecode, providing stable and reliable operation within this version.

## 2. Define a Object Relational Mapping (ORM) specification  

Now we define a declarative Object Relational Mapping (ORM) specification on those domain model classes mapping attributes of the conceptual JSON objects to the corresponding relational artifacts.

In `config` directory we create a `.jdx` file and define the ORM specification. 

The syntax for JDX_DATABASE for MySQL is:
```jdx
JDX_DATABASE JDX:jdbc:mysql://endpoint:port/nameOfDatabase
```

If you are not using database present on the cloud, use `host.docker.internal` as endpoint.

To learn more about the syntax and content of the `.jdx` file, refer Gilhari_README and the JDX Mannual provided in the SDK.

To make connection to the database we need JDBC driver of that RDBMS. So in `config` directory we add the database's JDBC driver as a `.jar`.  

> Gilhari framework ships three commonly used JDBC drivers in the directory `/node/node_modules/jdxnode/external_libs`  
But it is recommended to download and use the latest JDBC driver for your database.

To make our work simpler, we map "Employees" to the defined Employee container class. So we add a `.js` file in `config` directory. Repeat this for all the classes (shown in manyToManyExample).

Finally, create a `.config` file and fill in the required fields. It contains necessary configuration details for making connections to the database, debugging, ports, etc.

## 3. Create a Dockerfile, build and run Docker container  

The Gilhari microservice runs in a Docker container. We first need to build a docker image by combining various artifacts of our application.

Create a Dockerfile as shown and run the following command to build the docker image:  
```cmd
docker build -t gilhari2_hr_aws -f ./Dockerfile .
```

Run the docker image using the following command: 
```cmd
docker run -p 80:8081 gilhari2_hr_aws
```

If you are facing errors while running the docker container, try reading the error messages and search for fixes on the internet.

### If there were no errors, you have configured Gilhari successfully!
### Gilhari is now running on your localhost and you can make API calls through Postman.

>You an refer the Gilhari documentation for more information on the configuration process and the `.config` file and its fields.

Before proceeding forward, it is important to remove the old and failed docker images to keep the system clean. 

To remove docker images use the following commands:

```cmd
docker container prune
```

```cmd
docker image rm imageid
```

Sometimes images have to be forcefully removed using:

```cmd
docker rmi image_repository:image_tag
```

## Steps to change the RDBMS (or cloud platform)
To switch your RDBMS, you only need to make these 3 simple changes:  
1. Install the JDBC driver for your RDBMS and add it in the `config` directory
2. Change JDX_DATABASE and JDBC DRIVER information in the `.jdx` file in `config` directory 
3. Update the `jdbc_driver_path`, `db_username` and `db_password` in `.config` file

## Switching to AWS database  
Till now, we were using a database on our local machines. But, Gilhari can be used for databases on cloud platforms also. 

First create an account on AWS, then search `RDS` and create a DB Instance. You can get the endpoint for connection in the `Connectivity and Security` tab. Now follow the three steps for changing the RDBMS given above.

# Setting the project environment   
The two examples shown also contains Python scrips to generate dummy data through `faker` package and populate it into the database by making API calls through `requests` package.  

Install the latest version of Python from official sources.

## Creating Python virtual environment  

It's always a good idea to work on a virtual environment as it isolates the packages from the local machine.  
To create a virtual environment named `newvenv` use the following command in your terminal: 
```cmd
python -m venv newvenv
```

Once you have created a virtual environment, activate it by running this command:   

For windows:
```cmd
newvenv\Scripts\activate
```

For Unix or MacOS: 
```cmd
source newvenv/bin/activate
```

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using.

To deactivate the virtual environment use the following command:   
```cmd
deactivate
```

### You may face this error while activating your virtual environment:
>Running scripts is disabled on this system

This error occurs because the execution policy may be set to `Undefined` or `Restricted` which does not allow scripts to run.

To see the execution policy, open `windows powershell` and use the following command:
```cmd
Get-ExecutionPolicy
```

Set the execution policy to `RemoteSigned` 
```cmd
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

> You would have to run powershell as administrator for changing policy for localmachine scope

Click [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4) to learn more about execution policies.

## Making API calls 
Once Gilhari is listening at the localhost, we can use Postman for making API calls. Click [here](https://www.softwaretree.com/v1/products/gilhari/gilhari-restfulAPI.php) to know more about Gilhari RESTful APIs. A comprehensive guide for API usage can be found in the API documentation provided in the SDK.

## Running python scripts

To run the python scripts use the following command:

```cmd
python data_generator.py
```
```cmd
python transform.py
```
```cmd
python api_call.py
```
