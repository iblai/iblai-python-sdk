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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.crontab_schedule import CrontabSchedule
from typing import Optional, Set
from typing_extensions import Self

class PeriodicTask(BaseModel):
    """
    PeriodicTask
    """ # noqa: E501
    id: StrictInt
    name: StrictStr = Field(description="Short Description For This Task")
    crontab: CrontabSchedule
    one_off: Optional[StrictBool] = Field(default=None, description="If True, the schedule will only run the task a single time")
    start_time: Optional[datetime] = Field(default=None, description="Datetime when the schedule should begin triggering the task to run")
    enabled: Optional[StrictBool] = Field(default=None, description="Set to False to disable the schedule")
    __properties: ClassVar[List[str]] = ["id", "name", "crontab", "one_off", "start_time", "enabled"]

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
        """Create an instance of PeriodicTask from a JSON string"""
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
            "id",
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of crontab
        if self.crontab:
            _dict['crontab'] = self.crontab.to_dict()
        # set to None if start_time (nullable) is None
        # and model_fields_set contains the field
        if self.start_time is None and "start_time" in self.model_fields_set:
            _dict['start_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PeriodicTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "crontab": CrontabSchedule.from_dict(obj["crontab"]) if obj.get("crontab") is not None else None,
            "one_off": obj.get("one_off"),
            "start_time": obj.get("start_time"),
            "enabled": obj.get("enabled")
        })
        return _obj


