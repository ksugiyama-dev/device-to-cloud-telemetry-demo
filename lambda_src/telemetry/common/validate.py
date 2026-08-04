import json
import logging

def validate_get(event: dict, param: list):
    if "pathParameters" not in event or "edge_id" not in event["pathParameters"]:
        return False, "Missing edge_id in path parameters"

    if "queryStringParameters" not in event or not event["queryStringParameters"]:
        return False, "Missing query string parameters"
    
    if "start_timestamp" not in event["queryStringParameters"] or "end_timestamp" not in event["queryStringParameters"]:
        return False, "Missing start_timestamp or end_timestamp in query string parameters"

    if event.get("httpMethod") != 'GET':
        return False, f"Method {event.get('httpMethod')} not allowed"

    return True, None

def validate_post(event: dict, param: list, param2: list = []):
    if "body" not in event:
        return False, "Missing body in request"

    if event.get("httpMethod") != 'POST':
        return False, f"Method {event.get('httpMethod')} not allowed"

    try:
        body = event["body"]    
        for key, value in body.items():
            if key not in param:
                return False, f'Invalid key: {key}'
            
            if key == 'alerts' and isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        for alert_key in i.keys():
                            if alert_key not in param2:
                                return False, f'Invalid key in alert: {alert_key}'
                    else:
                        return False, f'Invalid alert item: {i}'

        # TelemetryDataPost.model_validate(body)
    except Exception as e:
        return False, f"Invalid telemetry data: {str(e)}"

    return True, None