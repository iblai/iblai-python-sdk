# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.google_pay_account_response_status_enum import GooglePayAccountResponseStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class GooglePayAccountResponse(BaseModel):
    """
    GooglePayAccountResponse
    """ # noqa: E501
    account_id: Annotated[str, Field(strict=True, max_length=255)]
    bundle_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default='', description="The bundle id of the app")
    status: Optional[GooglePayAccountResponseStatusEnum] = None
    created_on: datetime
    last_updated: datetime
    user: Optional[StrictInt] = Field(default=None, description="edX user ID")
    __properties: ClassVar[List[str]] = ["account_id", "bundle_id", "status", "created_on", "last_updated", "user"]

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
        """Create an instance of GooglePayAccountResponse from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_on",
            "last_updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GooglePayAccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_id": obj.get("account_id"),
            "bundle_id": obj.get("bundle_id") if obj.get("bundle_id") is not None else '',
            "status": obj.get("status"),
            "created_on": obj.get("created_on"),
            "last_updated": obj.get("last_updated"),
            "user": obj.get("user")
        })
        return _obj


