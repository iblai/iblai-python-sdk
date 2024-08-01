# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SlackConfig(BaseModel):
    """
    SlackConfig
    """ # noqa: E501
    id: StrictInt
    user: Annotated[int, Field(le=2147483647, strict=True, ge=0)] = Field(description="edX user ID")
    slack_team_domain: Annotated[str, Field(strict=True, max_length=200)] = Field(description="Team Domain in the stated slack workspace. This is also the workspace name.")
    slack_username: Annotated[str, Field(strict=True, max_length=200)] = Field(description="Username in the stated slack workspace")
    date_created: datetime
    last_modified: datetime
    __properties: ClassVar[List[str]] = ["id", "user", "slack_team_domain", "slack_username", "date_created", "last_modified"]

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
        """Create an instance of SlackConfig from a JSON string"""
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
            "user",
            "date_created",
            "last_modified",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlackConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user": obj.get("user"),
            "slack_team_domain": obj.get("slack_team_domain"),
            "slack_username": obj.get("slack_username"),
            "date_created": obj.get("date_created"),
            "last_modified": obj.get("last_modified")
        })
        return _obj


