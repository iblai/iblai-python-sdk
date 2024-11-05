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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from iblai.models.mentor_trace import MentorTrace
from typing import Optional, Set
from typing_extensions import Self

class MentorData(BaseModel):
    """
    MentorData
    """ # noqa: E501
    mentor: StrictStr
    total_cost: Union[StrictFloat, StrictInt]
    total_latency: Union[StrictFloat, StrictInt]
    mentor_traces: List[MentorTrace]
    __properties: ClassVar[List[str]] = ["mentor", "total_cost", "total_latency", "mentor_traces"]

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
        """Create an instance of MentorData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mentor_traces (list)
        _items = []
        if self.mentor_traces:
            for _item in self.mentor_traces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mentor_traces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MentorData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mentor": obj.get("mentor"),
            "total_cost": obj.get("total_cost"),
            "total_latency": obj.get("total_latency"),
            "mentor_traces": [MentorTrace.from_dict(_item) for _item in obj["mentor_traces"]] if obj.get("mentor_traces") is not None else None
        })
        return _obj


