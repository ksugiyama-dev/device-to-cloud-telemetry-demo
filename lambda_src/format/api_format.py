from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

class Alert(BaseModel):
    type: str
    message: str
    severity: Literal["info", "warning", "error", "critical"]
    timestamp: datetime

class TelemetryDataPost(BaseModel):
    edge_id: str = Field(required=True, description="Unique identifier for the edge device")
    timestamp: datetime = Field(required=True, description="Timestamp of the telemetry data")
    firmware_version: str = Field(required=True, description="Version of the firmware installed on the device")
    user_id: str = Field(required=True, description="Identifier for the user associated with the device")
    temperature: float = Field(ge=-50, le=150, description="Temperature in Celsius")
    humidity: float = Field(ge=0, le=100)
    pressure: float = Field(ge=300, le=1100)
    status: Literal["normal", "warning", "error", "offline"]
    battery_level: int = Field(ge=0, le=100)
    signal_strength: int = Field(ge=-100, le=0)
    error_codes: list[str] = Field(default=[], description="List of error codes reported by the device")
    last_maintenance: datetime = Field(description="Timestamp of the last maintenance check")
    alerts: list[Alert] = Field(default=[], description="List of alerts associated with the telemetry data")

class TelemetryDataGet(BaseModel):
    edge_id: str = Field(required=True, description="Unique identifier for the edge device")
    timestamp_start: datetime = Field(required=False, description="Start timestamp for the telemetry data range")
    timestamp_end: datetime = Field(required=False, description="End timestamp for the telemetry data range")
