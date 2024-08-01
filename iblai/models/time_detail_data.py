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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from iblai.models.time_detail_child import TimeDetailChild
from typing import Optional, Set
from typing_extensions import Self

class TimeDetailData(BaseModel):
    """
    TimeDetailData
    """ # noqa: E501
    average_time: Union[StrictFloat, StrictInt] = Field(description="Average time spent")
    display_name: StrictStr = Field(description="Chapter name")
    id: StrictStr = Field(description="Chapter Id")
    children: Optional[List[TimeDetailChild]] = None
    total_time: Optional[StrictInt] = Field(default=None, description="Total time spent")
    total_users: Optional[StrictInt] = Field(default=None, description="Total users who accessed the chapter")
    __properties: ClassVar[List[str]] = ["average_time", "display_name", "id", "children", "total_time", "total_users"]

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
        """Create an instance of TimeDetailData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item in self.children:
                if _item:
                    _items.append(_item.to_dict())
            _dict['children'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeDetailData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "average_time": obj.get("average_time"),
            "display_name": obj.get("display_name"),
            "id": obj.get("id"),
            "children": [TimeDetailChild.from_dict(_item) for _item in obj["children"]] if obj.get("children") is not None else None,
            "total_time": obj.get("total_time"),
            "total_users": obj.get("total_users")
        })
        return _obj


