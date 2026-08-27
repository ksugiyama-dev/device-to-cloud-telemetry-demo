import os
import boto3
from common.exceptions import UnprocessedItemsError

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

    if response['UnprocessedItems']:
        for i in range(10):  # Retry up to 10 times
            response = dynamodb.batch_write_item(
                RequestItems=response['UnprocessedItems']
            )
            if not response['UnprocessedItems']:
                break

            if i == 9:
                #　明日はここから
                unprocessed_items_list = [{
                    'edge_id': i['PutRequest']['Item']['edge_id']['S'],
                    'timestamp': i['PutRequest']['Item']['timestamp']['S']
                } for i in response['UnprocessedItems'][os.environ['TABLE_NAME']]]

                raise UnprocessedItemsError("Exceeded maximum retries for unprocessed items.\n" \
                f'Unprocessed items: {str(unprocessed_items_list)}')

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
