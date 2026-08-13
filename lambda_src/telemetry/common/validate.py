import json

def validate_get(event: dict):
    if "pathParameters" not in event or "edge_id" not in event["pathParameters"]:
        return False, "Missing edge_id in path parameters"

    if "queryStringParameters" not in event or not event["queryStringParameters"]:
        return False, "Missing query string parameters"
    
    if "start_timestamp" not in event["queryStringParameters"] or "end_timestamp" not in event["queryStringParameters"]:
        return False, "Missing start_timestamp or end_timestamp in query string parameters"

    return True, None

def validate_post(body: dict):

    required_item_list = [
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

    required_alert_item_list = [
        'type',
        'message',
        'severity',
        'timestamp'
    ]

    try:
        for key, value in body.items():
            if key not in required_item_list:
                return False, f'Invalid key: {key}'
            
            if key == 'alerts' and isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        for alert_key in i.keys():
                            if alert_key not in required_alert_item_list:
                                return False, f'Invalid key in alert: {alert_key}'
                    else:
                        return False, f'Invalid alert item: {i}'

        # TelemetryDataPost.model_validate(body)
    except Exception as e:
        return False, f"Invalid telemetry data: {str(e)}"

    return True, None