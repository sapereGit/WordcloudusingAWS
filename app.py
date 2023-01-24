#-*- coding: utf-8 -*-
__author__ = "Kevin shah(Sapere/GL)"
__license__ = "MIT"
__email__ = "kevin@globallingua.ca"
__maintainer__ = "Kevin shah(Sapere/GL)"

import json
import requests

def handler(event, context):

    # TODO implementation
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Lambda Container image invoked!",
                            "event": event})
    }