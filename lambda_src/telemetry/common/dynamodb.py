import json
import os
import logging
import boto3

from json_util import dict_to_dynamodb_json, dynamodb_json_to_dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def telemetry_data_post(body: dict):
    dynamodb = boto3.client('dynamodb')
    item = dict_to_dynamodb_json(body)

    logger.info(f'Putting item into DynamoDB: {item}')

    response = dynamodb.put_item(
        TableName=os.environ['TABLE_NAME'],
        Item=item
    )

    return response

def telemetry_data_get(edge_id: str, start_timestamp: str, end_timestamp: str) -> list:
    dynamodb = boto3.client('dynamodb')

    logger.info(f'Querying DynamoDB: {edge_id}, {start_timestamp}, {end_timestamp}')

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

    logger.info(f'Query response from DynamoDB: {response_db}')

    response = [dynamodb_json_to_dict(i) for i in response_db['Items']]

    return response
