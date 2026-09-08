import json
import pytest
from common.exceptions import UnprocessedItemsError

from common import dynamodb as dynamodb_common

def test_dynamodb_common_telemetry_data_get_1(mocker):
    
    edge_id = 'edge-001'
    start_timestamp = '2023-06-01T12:00:00Z'
    end_timestamp = '2023-06-01T13:00:00Z'

    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()

    mock_dynamodb.query.return_value = {
        'Items': [
            {
                "edge_id": {
                    "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                },
                "timestamp": {
                    "S": "2023-06-01T12:00:00Z"
                },
                "alerts": {
                    "L": [
                    {
                        "M": {
                        "timestamp": {
                            "S": "2023-06-01T11:45:00Z"
                        },
                        "message": {
                            "S": "Temperature exceeds threshold"
                        },
                        "severity": {
                            "S": "warning"
                        },
                        "type": {
                            "S": "temperature"
                        }
                        }
                    }
                    ]
                },
                "battery_level": {
                    "N": "85"
                },
                "error_codes": {
                    "L": []
                },
                "firmware_version": {
                    "S": "1.0.3"
                },
                "humidity": {
                    "N": "60.2"
                },
                "last_maintenance": {
                    "S": "2023-05-15T10:30:00Z"
                },
                "pressure": {
                    "N": "1013.25"
                },
                "signal_strength": {
                    "N": "-70"
                },
                "status": {
                    "S": "active"
                },
                "temperature": {
                    "N": "25.5"
                },
                "user_id": {
                    "S": "924f670e-9730-4eb3-a45a-d753badab738"
                }
            },
            {
                "edge_id": {
                    "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                },
                "timestamp": {
                    "S": "2023-06-01T13:00:00Z"
                },
                "alerts": {
                    "L": [
                    {
                        "M": {
                        "timestamp": {
                            "S": "2023-06-01T11:45:00Z"
                        },
                        "message": {
                            "S": "Temperature exceeds threshold"
                        },
                        "severity": {
                            "S": "warning"
                        },
                        "type": {
                            "S": "temperature"
                        }
                        }
                    }
                    ]
                },
                "battery_level": {
                    "N": "85"
                },
                "error_codes": {
                    "L": []
                },
                "firmware_version": {
                    "S": "1.0.3"
                },
                "humidity": {
                    "N": "60.2"
                },
                "last_maintenance": {
                    "S": "2023-05-15T10:30:00Z"
                },
                "pressure": {
                    "N": "1013.25"
                },
                "signal_strength": {
                    "N": "-70"
                },
                "status": {
                    "S": "active"
                },
                "temperature": {
                    "N": "26.5"
                },
                "user_id": {
                    "S": "924f670e-9730-4eb3-a45a-d753badab738"
                }
            }
        ]
    }

    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb
    )

    response = dynamodb_common.telemetry_data_get(edge_id, start_timestamp, end_timestamp)
    assert response == [
                {
                    "battery_level": 85,
                    "signal_strength": -70,
                    "status": "active",
                    "error_codes": [],
                    "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                    "temperature": 25.5,
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "pressure": 1013.25,
                    "alerts": [
                        {
                            "severity": "warning",
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ],
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "humidity": 60.2,
                    "firmware_version": "1.0.3",
                    "timestamp": "2023-06-01T12:00:00Z"
                },
                {
                    "battery_level": 85,
                    "signal_strength": -70,
                    "status": "active",
                    "error_codes": [],
                    "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                    "temperature": 26.5,
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "pressure": 1013.25,
                    "alerts": [
                        {
                            "severity": "warning",
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ],
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "humidity": 60.2,
                    "firmware_version": "1.0.3",
                    "timestamp": "2023-06-01T13:00:00Z"
                }
            ]

def test_dynamodb_common_telemetry_data_get_2(mocker):
    
    edge_id = 'edge-001'
    start_timestamp = '2023-06-01T12:00:00Z'
    end_timestamp = '2023-06-01T13:00:00Z'

    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()

    mock_dynamodb.query.return_value = {
        'Items': []
    }

    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb,
    )

    response = dynamodb_common.telemetry_data_get(edge_id, start_timestamp, end_timestamp)
    assert response == []

def test_dynamodb_common_telemetry_data_post_1(mocker):
    body = {
        'items': [
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T12:00:00Z"
            },
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T13:00:00Z"
            }
        ]
    }
    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()
    mock_dynamodb.batch_write_item.return_value = {
        'UnprocessedItems': {}
    }
    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb,
    )

    response = dynamodb_common.telemetry_data_post(body)
    assert response == {
        'UnprocessedItems': {}
    }
    mock_dynamodb.batch_write_item.assert_called_once_with(
        RequestItems={
            'mock-telemetry_history_table': [
                {
                    'PutRequest': {
                        'Item': {
                            "edge_id": {
                                "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                            },
                            "timestamp": {
                                "S": "2023-06-01T12:00:00Z"
                            },
                            "firmware_version": {
                                "S": "1.0.3"
                            },
                            "user_id": {
                                "S": "924f670e-9730-4eb3-a45a-d753badab738"
                            }
                        }
                    }
                },
                {
                    'PutRequest': {
                        'Item': {
                            "edge_id": {
                                "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                            },
                            "timestamp": {
                                "S": "2023-06-01T13:00:00Z"
                            },
                            "firmware_version": {
                                "S": "1.0.3"
                            },
                            "user_id": {
                                "S": "924f670e-9730-4eb3-a45a-d753badab738"
                            }
                        }
                    }
                }
            ]
        }
    )

def test_dynamodb_common_telemetry_data_post_2(mocker):
    body = {
        'items': [
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T12:00:00Z"
            },
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T13:00:00Z"
            }
        ]
    }

    requested_items_1 = {
        'mock-telemetry_history_table': [
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T12:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T13:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            }
        ]
    }

    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()
    mock_dynamodb.batch_write_item.side_effect = [
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': {}},
    ]

    expected_calls = [
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
    ]


    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb,
    )

    response = dynamodb_common.telemetry_data_post(body)


    assert response == {
        'UnprocessedItems': {}
    }
    assert mock_dynamodb.batch_write_item.call_count == 2

    assert mock_dynamodb.batch_write_item.call_args_list == expected_calls

def test_dynamodb_common_telemetry_data_post_3(mocker):
    body = {
        'items': [
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T12:00:00Z"
            },
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T13:00:00Z"
            }
        ]
    }

    requested_items_1 = {
        'mock-telemetry_history_table': [
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T12:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T13:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            }
        ]
    }

    requested_items_2 = {
        'mock-telemetry_history_table': [
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T13:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            }
        ]
    }

    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()
    mock_dynamodb.batch_write_item.side_effect = [
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': requested_items_2},
        {'UnprocessedItems': {}},
    ]

    expected_calls = [
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_2),
        mocker.call(RequestItems=requested_items_2),
        mocker.call(RequestItems=requested_items_2),
        mocker.call(RequestItems=requested_items_2),
        mocker.call(RequestItems=requested_items_2),
        mocker.call(RequestItems=requested_items_2), 
    ]


    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb,
    )

    response = dynamodb_common.telemetry_data_post(body)


    assert response == {
        'UnprocessedItems': {}
    }
    assert mock_dynamodb.batch_write_item.call_count == 11

    assert mock_dynamodb.batch_write_item.call_args_list == expected_calls

def test_dynamodb_common_telemetry_data_post_4(mocker):
    body = {
        'items': [
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T12:00:00Z"
            },
            {
                "edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                "timestamp": "2023-06-01T13:00:00Z"
            }
        ]
    }

    requested_items_1 = {
        'mock-telemetry_history_table': [
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T12:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T13:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            }
        ]
    }

    requested_items_2 = {
        'mock-telemetry_history_table': [
            {
                'PutRequest': {
                    'Item': {
                        "edge_id": {
                            "S": "2b1cf803-12c6-4984-9485-8d192e6c4864"
                        },
                        "timestamp": {
                            "S": "2023-06-01T13:00:00Z"
                        },
                        "firmware_version": {
                            "S": "1.0.3"
                        },
                        "user_id": {
                            "S": "924f670e-9730-4eb3-a45a-d753badab738"
                        }
                    }
                }
            }
        ]
    }

    mocker.patch.dict(
        dynamodb_common.os.environ,
        {'TABLE_NAME': 'mock-telemetry_history_table'}
    )

    mock_dynamodb = mocker.Mock()
    mock_dynamodb.batch_write_item.side_effect = [
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
        {'UnprocessedItems': requested_items_1},
    ]

    expected_calls = [
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
        mocker.call(RequestItems=requested_items_1),
    ]

    mocker.patch.object(
        dynamodb_common.boto3,
        'client',
        return_value = mock_dynamodb,
    )

    with pytest.raises(UnprocessedItemsError) as error_info:
        dynamodb_common.telemetry_data_post(body)

    assert "Exceeded maximum retries for unprocessed items. Unprocessed items: [{'edge_id': '2b1cf803-12c6-4984-9485-8d192e6c4864', 'timestamp': '2023-06-01T12:00:00Z'}, {'edge_id': '2b1cf803-12c6-4984-9485-8d192e6c4864', 'timestamp': '2023-06-01T13:00:00Z'}]" in str(error_info.value)
    assert mock_dynamodb.batch_write_item.call_count == 11

    assert mock_dynamodb.batch_write_item.call_args_list == expected_calls
