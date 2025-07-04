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

class PathwayCreateUpdateRequest(BaseModel):
    """
    Serializer for pathway creation/update request body.
    """ # noqa: E501
    pathway_id: Optional[StrictStr] = Field(default=None, description="Pathway ID")
    pathway_uuid: Optional[StrictStr] = Field(default=None, description="Pathway UUID")
    user_id: StrictInt = Field(description="User ID of the pathway owner")
    username: Optional[StrictStr] = Field(default=None, description="Username of the pathway owner")
    name: StrictStr = Field(description="Pathway name")
    slug: Optional[StrictStr] = Field(default=None, description="Pathway slug")
    visible: Optional[StrictBool] = Field(default=True, description="Whether the pathway is visible")
    platform_key: Optional[StrictStr] = Field(default=None, description="Platform key")
    path: List[Dict[str, Any]] = Field(description="List of items in the pathway with item_id and optional position")
    data: Optional[Any] = Field(default=None, description="Additional pathway data")
    __properties: ClassVar[List[str]] = ["pathway_id", "pathway_uuid", "user_id", "username", "name", "slug", "visible", "platform_key", "path", "data"]

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
        """Create an instance of PathwayCreateUpdateRequest from a JSON string"""
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
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathwayCreateUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pathway_id": obj.get("pathway_id"),
            "pathway_uuid": obj.get("pathway_uuid"),
            "user_id": obj.get("user_id"),
            "username": obj.get("username"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "visible": obj.get("visible") if obj.get("visible") is not None else True,
            "platform_key": obj.get("platform_key"),
            "path": obj.get("path"),
            "data": obj.get("data")
        })
        return _obj


