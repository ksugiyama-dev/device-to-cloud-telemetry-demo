import json
import logging
import boto3
import common.dynamodb as dynamodb_common

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

    valid, error_message = validate(event)

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
        dynamodb_common.telemetry_data_post(body)

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
        "body": json.dumps({
            "message": "Created telemetry data."
        })
    }


def validate(event: dict) -> tuple[bool, str]:
    if "body" not in event:
        return False, "Missing body in request"

    if event.get("httpMethod") != 'POST':
        return False, f"Method {event.get('httpMethod')} not allowed"

    try:
        body = event["body"]    
        for key, value in body.items():
            if key not in item_list:
                return False, f'Invalid key: {key}'
            
            if key == 'alerts' and isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        for alert_key in i.keys():
                            if alert_key not in alert_item_list:
                                return False, f'Invalid key in alert: {alert_key}'
                    else:
                        return False, f'Invalid alert item: {i}'

        # TelemetryDataPost.model_validate(body)
    except Exception as e:
        return False, f"Invalid telemetry data: {str(e)}"

    return True, None