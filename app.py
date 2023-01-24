#-*- coding: utf-8 -*-
__author__ = "Kevin shah(Sapere/GL)"
__license__ = "MIT"
__email__ = "kevin@globallingua.ca"
__maintainer__ = "Kevin shah(Sapere/GL)"
try:
        
    import json
    import requests
    import boto3
    print("All imports ok ...")
except Exception as e:
    print("Error Imports : {} ".format(e))


def handler(event, context):

    # TODO implementation
    s3_client = boto3.client('s3')
    s3_clientobj = s3_client.get_object(Bucket='lambdacontainerexecute', Key='tp-data.txt')

    for line in s3_clientobj['Body'].iter_lines():
        object = json.loads(line)
        print(f"Name: {object['name']['s']} ID: {object['id']['n']}")
    print("Welcome to SAPERE")
    print("Lambda execution Completed...!")
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Lambda Container image invoked!",
                            "event": event})
    }