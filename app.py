#-*- coding: utf-8 -*-
__author__ = "Kevin shah(Sapere/GL)"
__license__ = "MIT"
__email__ = "kevin@globallingua.ca"
__maintainer__ = "Kevin shah(Sapere/GL)"
try:
        
    import json
    import requests
    import boto3
    from wordcloud import WordCloud, STOPWORDS
    import os 
    os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
    import matplotlib.pyplot as plt
    import pandas as pd
    import re
    import string
    from PIL import Image
    import io
    print("All imports ok ...")
except Exception as e:
    print("Error Imports : {} ".format(e))


def save_to_bucket(wordcloud, bucket_name, filename):
    #Save tweet list to an s3 bucket
    BUCKET_NAME = bucket_name
    FILE_NAME = filename+'.png'
    s3_resource = boto3.resource('s3')
    object = s3_resource.Object(BUCKET_NAME, FILE_NAME)

    image_byte = image_to_byte_array(wordcloud.to_image())
    object.put(Body=image_byte)
    print("successfully put the image in container")

def image_to_byte_array(image, format: str = 'png'):
    result = io.BytesIO()
    image.save(result, format=format)
    result = result.getvalue()

    return result


def handler(event, context):

    # TODO implementation
    s3_client = boto3.client('s3')
    s3_clientobj = s3_client.get_object(Bucket='lambdacontainerexecute', Key='textfilename.txt')
    response_content = s3_clientobj['Body'].read()
    text = str(response_content.decode("utf-8", 'ignore')).replace("\r", "").replace("\n", " ")
    print("text:", text)
    comment_words = ''
    stopwords = set(STOPWORDS)
    s = text.split(' ')
    # iterate through the csv file
    for i in range(len(s)):
        s[i] = s[i].lower()

    # for line in s3_clientobj['Body'].iter_lines():
    #     object = json.loads(line)
    #     print(f"Name: {object['name']['s']} ID: {object['id']['n']}")
    print("Welcome to SAPERE")
    print("Lambda execution in process ...!")
    comment_words += " ".join(s) + " "
    wordcloud = WordCloud(width=1600, height=800, background_color='white', stopwords=stopwords, collocations=False,min_font_size=10).generate(comment_words)
    print(wordcloud)
    if wordcloud != None:
         textmessage = "Lambda execution Completed...!Wordcloud generted"
    else:
         textmessage = "Lambda Container image invoked and WORDCLOUD not DONE"

    save_to_bucket(wordcloud, 'outputbucketsapere', 'textfilename')
    print("ending")
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": textmessage,
                            "event": event})
    }