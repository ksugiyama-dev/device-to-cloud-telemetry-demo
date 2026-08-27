import json

from post import post as post_module
from common.exceptions import UnprocessedItemsError

def test_post_handler_valid_parameters_1(mocker):
    body = {
        "items": [
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
                "timestamp": "2023-06-01T12:01:00Z"
            },
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
                "timestamp": "2023-06-01T14:00:00Z"
            }
        ]
    }

    event = {
        "body" : json.dumps(body)
    }

    expected_data = json.dumps({})

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 201
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_called_once_with(body)
    
def test_post_handler_invalid_parameters_1(mocker):
    body = {
        "items": [
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
            }
        ]
    }

    event = {
        "items" : json.dumps(body)
    }

    expected_data = json.dumps({
        "error": "Missing request body"
    })

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 400
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_not_called()

def test_post_handler_invalid_parameters_2(mocker):
    body = """{
        "items": [
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
        ]
    }"""

    event = {
        "body" : body
    }

    expected_data = json.dumps({
        "error": "Invalid JSON in request body"
    })

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 400
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_not_called()

def test_post_handler_invalid_parameters_3(mocker):
    body = {
        "items": [
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
            }
        ]
    }

    event = {
        "items" : json.dumps(body)
    }

    expected_data = json.dumps({
        "error": "Missing request body"
    })

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 400
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_not_called()

def test_post_handler_valid_parameters_4(mocker):
    body = {
        "items": [
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:00Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:01Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:02Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:03Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:04Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:05Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:06Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:07Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:08Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:09Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:10Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },                    
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:11Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:12Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:13Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:14Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:15Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:16Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:17Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:18Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:19Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:20Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:21Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:22Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:23Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                "edge_id": "edge-001",
                "timestamp": "2023-06-01T12:00:24Z",
                "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                "firmware_version": "1.0.3",
                },
                {
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:25Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "firmware_version": "1.0.3",
                }
        ]
    }

    event = {
        "body" : json.dumps(body)
    }

    expected_data = json.dumps({
        "error": "'items' list cannot contain more than 25 items"
    })

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 400
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_not_called()


def test_post_handler_valid_parameters_5(mocker):
    body = {
        "items": [
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
            }
        ]
    }

    event = {
        "body" : json.dumps(body)
    }

    expected_data = json.dumps({
        "error": "Exceeded maximum retries for unprocessed items.\n" \
                f'Unprocessed items: {str({"edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864","timestamp": "2023-06-01T12:00:00Z"})}'
    })

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None,
        side_effect=UnprocessedItemsError("Exceeded maximum retries for unprocessed items.\n" \
                f'Unprocessed items: {str({"edge_id": "2b1cf803-12c6-4984-9485-8d192e6c4864","timestamp": "2023-06-01T12:00:00Z"})}')
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 429
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_called_once_with(body)

def test_post_handler_valid_parameters_6(mocker):
    body = {
        "items": [
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
            }
        ]
    }

    event = {
        "body" : json.dumps(body)
    }

    expected_data = json.dumps({"error": "Internal server error"})

    mock_telemetry_data_post = mocker.patch.object(
        post_module.dynamodb_common,
        "telemetry_data_post",
        return_value=None,
        side_effect=Exception("DynamoDB error")
    )

    response = post_module.handler(event, None)

    assert response["statusCode"] == 500
    assert response["body"] == expected_data
    mock_telemetry_data_post.assert_called_once_with(body)