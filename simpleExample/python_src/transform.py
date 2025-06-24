import json 

def transform_data(input_file, output_file):
    with open(input_file, 'r') as f:
        json_data = json.load(f) 

    transformed_data = {"entity": []} 
    for obj in json_data:
        transformed_obj = {
            "id": obj["id"],
            "name": obj["name"],
            "compensation": obj["compensation"],
            "exempt": obj["exempt"],
            "DOB": obj["DOB"]
        }
        transformed_data["entity"].append(transformed_obj)

    with open(output_file, 'w') as f:
        json.dump(transformed_data, f, indent = 4)

input_file = 'emp_data.json'
output_file = 'emp_data_transformed.json'

transform_data(input_file, output_file) 
print(f"Transformed data saved to '{output_file}'") 
