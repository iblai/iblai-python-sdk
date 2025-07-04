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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProgramInvitationRedemption(BaseModel):
    """
    Request serializer for ProgramInvitationRedemptionView POST endpoint
    """ # noqa: E501
    program_key: StrictStr = Field(description="The program key for the invitation")
    source: StrictStr = Field(description="The source identifier for the invitation")
    email: Optional[StrictStr] = Field(default=None, description="The email to associate with the invitation")
    username: Optional[StrictStr] = Field(default=None, description="The username to associate with the invitation")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata for the invitation")
    __properties: ClassVar[List[str]] = ["program_key", "source", "email", "username", "metadata"]

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
        """Create an instance of ProgramInvitationRedemption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProgramInvitationRedemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "program_key": obj.get("program_key"),
            "source": obj.get("source"),
            "email": obj.get("email"),
            "username": obj.get("username"),
            "metadata": obj.get("metadata")
        })
        return _obj


