import json
from datetime import datetime as dt

def validate_get(path_parameters: dict, query_parameters: dict):
    if "edge_id" not in path_parameters:
        return False, "Missing edge_id in path parameters"

    elif not isinstance(path_parameters["edge_id"], str) or not path_parameters["edge_id"]:
        return False, "Invalid edge_id format"
    
    if "start_timestamp" not in query_parameters:
        return False, "Missing start_timestamp in query string parameters"

    if "end_timestamp" not in query_parameters:
        return False, "Missing end_timestamp in query string parameters"

    if not isinstance(query_parameters["start_timestamp"], str):
        return False, "Invalid start_timestamp format"

    if not isinstance(query_parameters["end_timestamp"], str):
        return False, "Invalid end_timestamp format"
    
    try:
        start_timestamp = dt.strptime(query_parameters["start_timestamp"], '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return False, "Invalid start_timestamp format"

    try:
        end_timestamp = dt.strptime(query_parameters["end_timestamp"], '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return False, "Invalid end_timestamp format"

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

            if key == 'alerts':
                if isinstance(value, list):
                    for i in value:
                        if isinstance(i, dict):
                            for alert_key in i.keys():
                                if alert_key not in alert_item_list:
                                    return False, f'Invalid key in alert: {alert_key}'
                        else:
                            return False, f'Invalid alert item: {i}'
                else:
                    return False, f'Invalid alerts value: {value}'

        # TelemetryDataPost.model_validate(body)
    except Exception as e:
        return False, f"Invalid telemetry data: {str(e)}"

    return True, None