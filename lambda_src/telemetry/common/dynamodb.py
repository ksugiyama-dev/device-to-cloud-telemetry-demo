import json
import os
import logging
from decimal import Decimal
import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

serializer = TypeSerializer()
deserializer = TypeDeserializer()

def telemetry_data_post(body: dict):
    dynamodb = boto3.client('dynamodb')
    item = dict_to_dynamodb_json(body)

    logger.info(f'Putting item into DynamoDB: {item}')

    dynamodb.put_item(
        TableName=os.environ['TABLE_NAME'],
        Item=item
    )

def telemetry_data_get(body: dict) -> list:
    dynamodb = boto3.client('dynamodb')

    logger.info(f'Querying DynamoDB: {body}')

    response_db = dynamodb.query(
        TableName=os.environ['TABLE_NAME'],
        KeyConditionExpression='edge_id = :edge_id AND #ts BETWEEN :start_ts AND :end_ts',
        ExpressionAttributeNames={
            '#ts': 'timestamp'
        },
        ExpressionAttributeValues={
            ':edge_id': {'S': body['edge_id']},
            ':start_ts': {'S': str(body['start_timestamp'])},
            ':end_ts': {'S': str(body['end_timestamp'])}
        }
    )

    logger.info(f'Query response from DynamoDB: {response_db}')

    response = [dynamodb_json_to_dict(i) for i in response_db['Items']]

    return response

def dict_to_dynamodb_json(dict_data: dict) -> dict:
    dict_decimal = float_to_decimal(dict_data)
    dynamodb_json = {
        k: serializer.serialize(v)
        for k, v in dict_decimal.items()
        }

    return dynamodb_json

def float_to_decimal(value) -> dict:
    if isinstance(value, list):
        return [float_to_decimal(i) for i in value]
    elif isinstance(value, dict):
        return {k: float_to_decimal(v) for k, v in value.items()}
    elif isinstance(value, float):
        return Decimal(str(value))
    else:
        return value

def dynamodb_json_to_dict(dynamodb_json: dict) -> dict:
    dict_data = {
        k: deserializer.deserialize(v) 
        for k, v in dynamodb_json.items()
        }
    
    return decimal_to_float(dict_data)


def decimal_to_float(value) -> dict:
    if isinstance(value, list):
        return [decimal_to_float(i) for i in value]
    elif isinstance(value, dict):
        return {k: decimal_to_float(v) for k, v in value.items()}
    elif isinstance(value, Decimal):
        if value %1 ==0:
            return int(value)
        return float(value)
    else:
        return value