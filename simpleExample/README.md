# HR Management in relational database using Gilhari

## Gilhari2_HR_AWS 

This is a simple case scenerio where the HR Manager stores the employee details in a database. 

Employee details include `id`, `name`, `exempt`, `compensation` and `compensation`. `id` is the primary key.

To add other constraints, you would have to mention them in the `.jdx` file in `config` directory.

## python_src

`data_generator.py` will generate dummy data for testing and store them in `emp_data.json`.

`transform.py` will transform the generated data into the format required for sending the data through POST API call, and store it in `emp_data_transformed.json`.

You can then make API calls by running `api_call.py`.