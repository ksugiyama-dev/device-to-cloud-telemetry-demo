from common.validate import validate_get, validate_post

# Test of validate_get function
def test_validate_get_accepts_valid_parameters():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is True
    assert error_message is None

def test_validate_get_rejects_invalid_edge_id():
    path_parameters = {}
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Missing edge_id in path parameters"

def test_validate_get_rejects_invalid_edge_id_format_1():
    path_parameters = {
        "edge_id": "",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid edge_id format"

def test_validate_get_rejects_invalid_edge_id_format_2():
    path_parameters = {
        "edge_id": 12345,
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid edge_id format"

def test_validate_get_rejects_invalid_edge_id_format_3():
    path_parameters = {
        "edge_id": 12345,
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid edge_id format"

def test_validate_get_rejects_invalid_edge_id_format_4():
    path_parameters = {
        "edge_id": None,
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid edge_id format"

def test_validate_get_rejects_missing_start_timestamp():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Missing start_timestamp in query string parameters"

def test_validate_get_rejects_invalid_start_timestamp_1():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid start_timestamp format"

def test_validate_get_rejects_invalid_start_timestamp_2():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00",
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid start_timestamp format"

def test_validate_get_rejects_invalid_start_timestamp_3():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": None,
        "end_timestamp": "2026-08-17T11:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid start_timestamp format"

def test_validate_get_rejects_missing_end_timestamp():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Missing end_timestamp in query string parameters"

def test_validate_get_rejects_invalid_end_timestamp_1():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid end_timestamp format"

def test_validate_get_rejects_invalid_end_timestamp_2():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": "2026-08-17T11:00:00",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid end_timestamp format"

def test_validate_get_rejects_invalid_end_timestamp_3():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T10:00:00Z",
        "end_timestamp": None,
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "Invalid end_timestamp format"

def test_validate_get_rejects_invalid_end_is_earlier_than_start():
    path_parameters = {
        "edge_id": "device-001",
    }
    query_parameters = {
        "start_timestamp": "2026-08-17T11:00:00Z",
        "end_timestamp": "2026-08-17T10:00:00Z",
    }

    valid, error_message = validate_get(path_parameters, query_parameters)

    assert valid is False
    assert error_message == "start_timestamp cannot be greater than end_timestamp"

# Test of validate_post function
def test_validate_post_accepts_valid_parameters_1():
    body = {
                'items': [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is True
    assert error_message is None

def test_validate_post_accepts_valid_parameters_2():
    body = {
                'items': [
                    {
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "firmware_version": "1.0.3",
                    }
                ]
            }

    valid, error_message = validate_post(body)

    assert valid is True
    assert error_message is None

def test_validate_post_accepts_valid_parameters_3():
    body = {
                'items': [
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
                    }
                ]
            }

    valid, error_message = validate_post(body)

    assert valid is True
    assert error_message is None

def test_validate_post_rejects_missing_edge_id():
    body = {
                "items" : [{
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Missing required key: edge_id"

def test_validate_post_rejects_missing_timestamp():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Missing required key: timestamp"

def test_validate_post_rejects_missing_firmware_version():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Missing required key: firmware_version"

def test_validate_post_rejects_missing_user_id():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Missing required key: user_id"

def test_validate_post_rejects_invalid_parameters_1():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temp": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Invalid key: temp"

def test_validate_post_rejects_invalid_parameters_2():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": 
                        {
                            "type": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                }]
                
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Invalid alerts value: {'type': 'temperature', 'message': 'Temperature exceeds threshold', 'severity': 'warning', 'timestamp': '2023-06-01T11:45:00Z'}"

def test_validate_post_rejects_invalid_parameters_3():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                        {
                            "typ": "temperature",
                            "message": "Temperature exceeds threshold",
                            "severity": "warning",
                            "timestamp": "2023-06-01T11:45:00Z"
                        }
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Invalid key in alert: typ"

def test_validate_post_rejects_invalid_parameters_4():
    body = {
                "items" : [{
                    "edge_id": "edge-001",
                    "timestamp": "2023-06-01T12:00:00Z",
                    "user_id": "924f670e-9730-4eb3-a45a-d753badab738",
                    "temperature": 25.5,
                    "humidity": 60.2,
                    "pressure": 1013.25,
                    "status": "active",
                    "battery_level": 85,
                    "signal_strength": -70,
                    "error_codes": [],
                    "firmware_version": "1.0.3",
                    "last_maintenance": "2023-05-15T10:30:00Z",
                    "alerts": [
                            "temperature",
                            "Temperature exceeds threshold",
                            "warning",
                            "2023-06-01T11:45:00Z"
                        
                    ]
                }]
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "Invalid alert item: temperature"

def test_validate_post_rejects_invalid_parameters_5():
    body = {
                "items" : "item"
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "'items' must be a list"

def test_validate_post_rejects_invalid_parameters_6():
    body = {
                "items" : []
            }

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "'items' list cannot be empty"

def test_validate_post_rejects_invalid_parameters_7():
    body = {
                'items': [
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

    valid, error_message = validate_post(body)

    assert valid is False
    assert error_message == "'items' list cannot contain more than 25 items"