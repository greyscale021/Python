# Lambda function 

instances = [{"id": "i-3", "cpu": 80}, {"id": "i-2", "cpu": 20}, {"id": "i-1", "cpu": 10}, {"id": "i-9", "cpu": 0}]
# List of dictionaries

instances.sort(key=lambda x:x["cpu"])   # Using lambda function to sort by key: "cpu"
for i in instances:
    print(i)
