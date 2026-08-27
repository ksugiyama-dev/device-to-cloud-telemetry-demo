import os
import json
import logging
from common.exceptions import UnprocessedItemsError

import common.dynamodb as dynamodb_common
from common.validate import validate_post
# from lambda_src.format.api_format import TelemetryDataPost

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

def handler(event, context):
    if not event.get('body'):
        logger.warning("Missing request body")
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "Missing request body"
            })
        }

    try:
        body: dict = json.loads(event['body'])

    except json.JSONDecodeError:
        logger.warning("Invalid JSON in request body")
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "Invalid JSON in request body"
            })
        }

    valid, error_message = validate_post(body)

    if not valid:
        logger.warning(f"Invalid request body: {error_message}")
        return {
            "statusCode": 400,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": error_message
            })
        }

    logger.info(f"Received telemetry data: edge_id={body.get('edge_id')}, timestamp={body.get('timestamp')}")

    try:
        response = dynamodb_common.telemetry_data_post(body)
        logger.info(f"Successfully saved telemetry data to DynamoDB: edge_id={body.get('edge_id')}, timestamp={body.get('timestamp')}")

    except UnprocessedItemsError as e:
        logger.warning(f'Unprocessed items error: {e}')
        return {
            "statusCode": 429,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }

    except Exception:
        logger.exception(f"Error occurred while saving data to DynamoDB")
        return {
            "statusCode": 500,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps({
                "error": "Internal server error"
            })
        }

    return {
        "statusCode": 201,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps({})
    }
