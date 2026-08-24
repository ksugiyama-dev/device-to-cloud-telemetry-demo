from decimal import Decimal
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

def dict_to_dynamodb_json(items: list) -> list:
    return_items = []
    for item in items:
        serializer = TypeSerializer()

        dict_decimal = float_to_decimal(item)
        return_items.append ({
            k: serializer.serialize(v)
            for k, v in dict_decimal.items()
            })

    return return_items

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
    deserializer = TypeDeserializer()
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