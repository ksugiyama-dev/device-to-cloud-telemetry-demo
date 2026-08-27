import json

from get import get as get_module

def test_get_handler_valid_parameters_1(mocker):
    event = {
        "pathParameters": {
            "edge_id": "edge-001"
        },
        "queryStringParameters": {
            "start_timestamp": "2023-06-01T12:00:00Z",
            "end_timestamp": "2023-06-01T13:00:00Z"
        }
    }

    expected_data = [
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

    mock_telemetry_data_get = mocker.patch.object(
        get_module.dynamodb_common,
        "telemetry_data_get",
        return_value=expected_data
    )

    response = get_module.handler(event, None)

    assert response["statusCode"] == 200
    assert response["body"] == json.dumps({"items": expected_data })
    mock_telemetry_data_get.assert_called_once_with(
        "edge-001",
        "2023-06-01T12:00:00Z",
        "2023-06-01T13:00:00Z"
    )


def test_get_handler_valid_parameters_2(mocker):
    event = {
        "pathParameters": {
            "edge_id": "edge-001"
        },
        "queryStringParameters": {
            "start_timestamp": "2023-06-01T12:00:00Z",
            "end_timestamp": "2023-06-01T13:00:00Z"
        }
    }

    expected_data = []

    mock_telemetry_data_get = mocker.patch.object(
        get_module.dynamodb_common,
        "telemetry_data_get",
        return_value=expected_data
    )

    response = get_module.handler(event, None)

    assert response["statusCode"] == 200
    assert response["body"] == json.dumps({"items": expected_data })
    mock_telemetry_data_get.assert_called_once_with(
        "edge-001",
        "2023-06-01T12:00:00Z",
        "2023-06-01T13:00:00Z"
    )

def test_get_handler_invalid_parameters(mocker):
    event = {
        "queryStringParameters": {
            "start_timestamp": "2023-06-01T12:00:00Z",
            "end_timestamp": "2023-06-01T13:00:00Z"
        }
    }

    response = get_module.handler(event, None)

    assert response["statusCode"] == 400
    assert response["body"] == json.dumps({"error": "Missing edge_id in path parameters"})

def test_get_handler_dynamodb_error(mocker):
    event = {
        "pathParameters": {
            "edge_id": "edge-001"
        },
        "queryStringParameters": {
            "start_timestamp": "2023-06-01T12:00:00Z",
            "end_timestamp": "2023-06-01T13:00:00Z"
        }
    }

    mock_telemetry_data_get = mocker.patch.object(
        get_module.dynamodb_common,
        "telemetry_data_get",
        side_effect=Exception("DynamoDB error")
    )

    response = get_module.handler(event, None)

    assert response["statusCode"] == 500
    assert response["body"] == json.dumps({"error": "Internal server error"})
    mock_telemetry_data_get.assert_called_once_with(
        "edge-001",
        "2023-06-01T12:00:00Z",
        "2023-06-01T13:00:00Z"
    )