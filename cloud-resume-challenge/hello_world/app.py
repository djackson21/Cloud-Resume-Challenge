import json
import boto3
# import requests

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    
    response = table.get_item(
        Key = {
            'ID':'visitors'
        }
    )
    
    visit_count = response['Item']['counter'] 
    visit_count = str(int(visit_count) + 1)
    
    response = table.put_item(
        Item = {
            'ID':'visitors',
            'counter': visit_count
        }
    )


    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps(
            {'visit_count': visit_count})
    }
