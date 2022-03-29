from __future__ import annotations
from turtle import st

from typing import Any, Optional

from pydantic import BaseModel


class Destination(BaseModel):
    destinationType: str
    name: str


class IdxGroupID(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogDestination(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogType(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogDescription(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogDirection(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxMethod(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxTotal(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: int
    long: Any
    float: Any
    double: Any
    string: Any
    bytes: Any


class LogStatus(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxCmdType(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxSender(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogConsumer(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxCorrelationID(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxFlowType(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxFileType(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogEvent(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogSender(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class LogTimestamp(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class _AMQCID(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class BreadcrumbId(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxFileName(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxReplyTo(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class IdxNumber(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: int
    long: Any
    float: Any
    double: Any
    string: Any
    bytes: Any


class LogByteMessageIdentity(BaseModel):
    propertyType: str
    boolean: Any
    byte: Any
    short: Any
    integer: Any
    long: Any
    float: Any
    double: Any
    string: str
    bytes: Any


class Properties(BaseModel):
    idxGroupID: IdxGroupID
    logDestination: LogDestination
    logType: LogType
    logDescription: LogDescription
    logDirection: LogDirection
    idxMethod: IdxMethod
    idxTotal: IdxTotal
    logStatus: LogStatus
    idxCmdType: IdxCmdType
    idxSender: IdxSender
    logConsumer: LogConsumer
    idxCorrelationID: IdxCorrelationID
    idxFlowType: IdxFlowType
    idxFileType: IdxFileType
    logEvent: LogEvent
    logSender: LogSender
    logTimestamp: LogTimestamp
    __AMQ_CID: _AMQCID
    breadcrumbId: BreadcrumbId
    idxFileName: IdxFileName
    idxReplyTo: IdxReplyTo
    idxNumber: IdxNumber
    logByteMessageIdentity: LogByteMessageIdentity


class Model(BaseModel):
    messageID: str
    messageType: str
    timestamp: int
    deliveryMode: int
    correlationID: Any
    replyTo: Any
    destination: Destination
    redelivered: bool
    type: Any
    expiration: int
    priority: int
    properties: Properties
    bytes: str
    map: Any
    text: Any
