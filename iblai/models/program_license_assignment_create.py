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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProgramLicenseAssignmentCreate(BaseModel):
    """
    Request serializer for ProgramLicenseAssignmentView POST endpoint.  This serializer validates the request data for creating or updating a program license assignment. Either user_id or email must be provided to identify the user to assign the license to.  Fields:     license_id: The ID of the program license to assign     user_id: The user ID to assign the license to (required if email not provided)     username: The username to assign the license to (alternative to user_id)     email: The email to assign the license to (required if user_id not provided)     platform_key: The unique identifier for the platform (for permission validation)     platform_org: The organization identifier for the platform (for permission validation)     active: Whether the assignment should be active     fulfilled: Whether the assignment should be marked as fulfilled     direct: Whether the assignment is being directly assigned to the user     redirect_to: URL to redirect to after fulfillment     metadata: Additional metadata for the assignment  Notes:     - If both user_id and email are provided, user_id takes precedence     - If the user doesn't exist but email is provided, an email-only assignment will be created     - The license must have available seats for the assignment to succeed
    """ # noqa: E501
    license_id: StrictInt = Field(description="The ID of the program license to assign")
    user_id: Optional[StrictInt] = Field(default=None, description="The user ID to assign the license to (required if email not provided)")
    username: Optional[StrictStr] = Field(default=None, description="The username to assign the license to (alternative to user_id)")
    email: Optional[StrictStr] = Field(default=None, description="The email to assign the license to (required if user_id not provided)")
    platform_key: Optional[StrictStr] = Field(default=None, description="The unique identifier for the platform (for permission validation)")
    platform_org: Optional[StrictStr] = Field(default=None, description="The organization identifier for the platform (for permission validation)")
    active: Optional[StrictBool] = Field(default=True, description="Whether the assignment should be active")
    fulfilled: Optional[StrictBool] = Field(default=False, description="Whether the assignment should be marked as fulfilled")
    direct: Optional[StrictBool] = Field(default=True, description="Whether the assignment is being directly assigned to the user")
    redirect_to: Optional[StrictStr] = Field(default=None, description="URL to redirect to after fulfillment")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata for the assignment")
    __properties: ClassVar[List[str]] = ["license_id", "user_id", "username", "email", "platform_key", "platform_org", "active", "fulfilled", "direct", "redirect_to", "metadata"]

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
        """Create an instance of ProgramLicenseAssignmentCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if redirect_to (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_to is None and "redirect_to" in self.model_fields_set:
            _dict['redirect_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProgramLicenseAssignmentCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "license_id": obj.get("license_id"),
            "user_id": obj.get("user_id"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "platform_key": obj.get("platform_key"),
            "platform_org": obj.get("platform_org"),
            "active": obj.get("active") if obj.get("active") is not None else True,
            "fulfilled": obj.get("fulfilled") if obj.get("fulfilled") is not None else False,
            "direct": obj.get("direct") if obj.get("direct") is not None else True,
            "redirect_to": obj.get("redirect_to"),
            "metadata": obj.get("metadata")
        })
        return _obj


