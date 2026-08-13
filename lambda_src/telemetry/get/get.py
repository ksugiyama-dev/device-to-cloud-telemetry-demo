import os
import json
import logging

import common.dynamodb as dynamodb_common
from common.validate import validate_get

# from lambda_src.format.api_format import TelemetryDataGet

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

def handler(event, context):
    logger.info(f"Received event: edge_id={event.get('pathParameters', {}).get('edge_id')}, start_timestamp={event.get('queryStringParameters', {}).get('start_timestamp')}, end_timestamp={event.get('queryStringParameters', {}).get('end_timestamp')}")
    valid, error_message = validate_get(event)

    if not valid:
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": error_message
            })
        }
    
    # body: TelemetryDataGet = event["body"]
    edge_id: str = event.get('pathParameters', {}).get('edge_id')
    start_timestamp: str = event.get('queryStringParameters', {}).get('start_timestamp')
    end_timestamp: str = event.get('queryStringParameters', {}).get('end_timestamp')

    try:
        response = dynamodb_common.telemetry_data_get(edge_id, start_timestamp, end_timestamp)

    except Exception as e:
        logger.exception(f"Error occurred while fetching data from DynamoDB: {e}")
        return {
            "statusCode": 500,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "Internal server error"
            })
        }
    
    if not response:
        logger.info(f"Get Telemetry Data successful: edge_id={edge_id}, start_timestamp={start_timestamp}, end_timestamp={end_timestamp}")
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({})
        }
    logger.info(f"Get Telemetry Data successful: edge_id={edge_id}, start_timestamp={start_timestamp}, end_timestamp={end_timestamp}")
    return {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps({
            "items": response
        })
    }
