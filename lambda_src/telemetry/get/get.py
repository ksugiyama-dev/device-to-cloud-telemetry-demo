import json
import logging

import common.dynamodb as dynamodb_common
from common.validate import validate_get

# from lambda_src.format.api_format import TelemetryDataGet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

item_list = [
    'edge_id',
    'start_timestamp',
    'end_timestamp'
]

def handler(event, context):
    logger.info(f"Received event: {event}")
    valid, error_message = validate_get(event, item_list)

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
    body: dict = event["body"]

    try:
        response = dynamodb_common.telemetry_data_get(body)

    except Exception as e:
        logger.error(f"Error occurred while fetching data from DynamoDB: {e}")
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
        return {
            "statusCode": 404,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "No telemetry data found for the given edge_id and timestamp range"
            })
        }
    logger.info(f"Return value: {response}")
    return {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps({
            "items": response
        })
    }
