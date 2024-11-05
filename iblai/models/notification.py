# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.message_status import MessageStatus
from typing import Optional, Set
from typing_extensions import Self

class Notification(BaseModel):
    """
    Notification
    """ # noqa: E501
    id: StrictStr
    username: StrictStr
    title: StrictStr
    body: StrictStr
    status: Optional[MessageStatus] = None
    channel: Optional[StrictInt] = None
    context: Optional[Any] = None
    short_message: StrictStr
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "username", "title", "body", "status", "channel", "context", "short_message", "created_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Notification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "title",
            "body",
            "short_message",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if channel (nullable) is None
        # and model_fields_set contains the field
        if self.channel is None and "channel" in self.model_fields_set:
            _dict['channel'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "title": obj.get("title"),
            "body": obj.get("body"),
            "status": MessageStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "channel": obj.get("channel"),
            "context": obj.get("context"),
            "short_message": obj.get("short_message"),
            "created_at": obj.get("created_at")
        })
        return _obj


