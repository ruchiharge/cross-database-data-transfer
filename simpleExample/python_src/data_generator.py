import json 
import random 
import time 
import datetime 
from faker import Faker 

fake = Faker() 

# function for generating single record
def generate_record(record_id):
    # generating date and converting it into milliseconds since January 1, 1970
    dob = fake.date_of_birth(minimum_age = 18, maximum_age = 65)
    dob_datetime = datetime.datetime(dob.year, dob.month, dob.day) 
    dob_milliseconds = int(time.mktime(dob_datetime.timetuple()) * 1000)

    return {
        "id": record_id,
        "name": fake.name(),
        "compensation": random.randint(3, 12) * 10000,
        "exempt": random.choice([True, False]),
        "DOB": dob_milliseconds
    }

# generate 50 records
data = [generate_record(i) for i in range(1, 51)]

# save to a JSON file
with open('emp_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data generated and saved to emp_data.json")
