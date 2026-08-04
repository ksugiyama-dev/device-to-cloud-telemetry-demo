import json
import logging

import common.dynamodb as dynamodb_common
from common.validate import validate_post
# from lambda_src.format.api_format import TelemetryDataPost

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

item_list = [
    'edge_id',
    'timestamp',
    'firmware_version',
    'user_id',
    'temperature',
    'humidity',
    'pressure',
    'status',
    'battery_level',
    'signal_strength',
    'error_codes',
    'last_maintenance',
    'alerts'
]

alert_item_list = [
    'type',
    'message',
    'severity',
    'timestamp'
]

def handler(event, context):
    logger.info(f"Received event: {event}")

    valid, error_message = validate_post(event)

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
    
    # body: TelemetryDataPost = event["body"]
    body: dict = event["body"]

    try:
        response = dynamodb_common.telemetry_data_post(body, item_list, alert_item_list)
        logger.info(f"Successfully saved telemetry data to DynamoDB: {response}")

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }

    except Exception as e:
        logger.error(f"Error occurred while saving data to DynamoDB: {e}")
        return {
            "statusCode": 500,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "Internal server error"
            })
        }
    
    logger.info(f"Received event: {event}")

    return {
        "statusCode": 201,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps({})
    }
