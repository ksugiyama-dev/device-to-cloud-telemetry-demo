from datetime import datetime as dt

def validate_get(event: dict):
    if "pathParameters" not in event or "edge_id" not in event["pathParameters"]:
        return False, "Missing edge_id in path parameters"

    if "queryStringParameters" not in event or not event["queryStringParameters"]:
        return False, "Missing query string parameters"
    
    if "start_timestamp" not in event["queryStringParameters"] or "end_timestamp" not in event["queryStringParameters"]:
        return False, "Missing start_timestamp or end_timestamp in query string parameters"

    try:
        start_timestamp = dt.strptime(event["queryStringParameters"]["start_timestamp"], '%Y-%m-%dT%H:%M:%SZ')
        end_timestamp = dt.strptime(event["queryStringParameters"]["end_timestamp"], '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return False, "Invalid timestamp format"

    if start_timestamp > end_timestamp:
        return False, "start_timestamp cannot be greater than end_timestamp"

    return True, None

def validate_post(body: dict):
    required_item_list = [
        'edge_id',
        'timestamp',
        'firmware_version',
        'user_id'
    ]

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
    # Validate that all required values are present.
    for key in required_item_list:
        if key not in body:
            return False, f'Missing required key: {key}'

    # Validate that unexpected values are not present and that the values are of the correct type.
    try:
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