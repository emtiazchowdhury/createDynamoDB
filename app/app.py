import json
import boto3

# Get the service resource
client = boto3.client('dynamodb')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    try:
        if event['httpMethod'] == 'GET':
            client.get_item(
                TableName="CollegeApplicantDatabase",
                Key={
                    'lastname':
                        {'S': body['lastname']},
                    'email':
                        {'S': body['email']}
                }
            )
        elif event['httpMethod'] == "PUT":
            putrecord = {
                "lastname": {
                    "S": body['lastname']
                },
                "email": {
                    "S": body['email']
                },
                "major": {
                    "S": body['major']
                },
                "phone": {
                    "S": body['phone']
                }
            }
            client.put_item(TableName='CollegeApplicantDatabase', Item=putrecord)
    except Exception as e:
        # Handle the exception
        print("An error occurred:", e)
        return {
            "statusCode": 500,
            "body": "Internal Server Error"
        }

    return {
        "statusCode": 200,
        "body": json.dumps('Operation Successful')
    }
