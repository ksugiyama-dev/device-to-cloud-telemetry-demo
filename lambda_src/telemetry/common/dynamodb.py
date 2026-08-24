import os
import boto3

from common.json_util import (dict_to_dynamodb_json, dynamodb_json_to_dict)

def telemetry_data_post(body: dict):
    dynamodb = boto3.client('dynamodb')
    items: list = dict_to_dynamodb_json(body['items'])

    response = dynamodb.batch_write_item(
        RequestItems={
            os.environ['TABLE_NAME']: [
                {
                    'PutRequest': {
                        'Item': item
                    }
                }
            ] for item in items
        }
    )

    return response

def telemetry_data_get(edge_id: str, start_timestamp: str, end_timestamp: str) -> list:
    dynamodb = boto3.client('dynamodb')

    response_db = dynamodb.query(
        TableName=os.environ['TABLE_NAME'],
        KeyConditionExpression='edge_id = :edge_id AND #ts BETWEEN :start_ts AND :end_ts',
        ExpressionAttributeNames={
            '#ts': 'timestamp'
        },
        ExpressionAttributeValues={
            ':edge_id': {'S': edge_id},
            ':start_ts': {'S': start_timestamp},
            ':end_ts': {'S': end_timestamp}
        }
    )

    response = [dynamodb_json_to_dict(i) for i in response_db['Items']]

    return response
