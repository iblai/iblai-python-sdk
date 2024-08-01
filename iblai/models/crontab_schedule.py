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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CrontabSchedule(BaseModel):
    """
    CrontabSchedule
    """ # noqa: E501
    minute: Optional[Annotated[str, Field(strict=True, max_length=240)]] = Field(default=None, description="Cron Minutes to Run. Use \"*\" for \"all\". (Example: \"0,30\")")
    hour: Optional[Annotated[str, Field(strict=True, max_length=96)]] = Field(default=None, description="Cron Hours to Run. Use \"*\" for \"all\". (Example: \"8,20\")")
    day_of_week: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Cron Days Of The Week to Run. Use \"*\" for \"all\", Sunday is 0 or 7, Monday is 1. (Example: \"0,5\")")
    day_of_month: Optional[Annotated[str, Field(strict=True, max_length=124)]] = Field(default=None, description="Cron Days Of The Month to Run. Use \"*\" for \"all\". (Example: \"1,15\")")
    month_of_year: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="Cron Months (1-12) Of The Year to Run. Use \"*\" for \"all\". (Example: \"1,12\")")
    __properties: ClassVar[List[str]] = ["minute", "hour", "day_of_week", "day_of_month", "month_of_year"]

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
        """Create an instance of CrontabSchedule from a JSON string"""
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
        """Create an instance of CrontabSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minute": obj.get("minute"),
            "hour": obj.get("hour"),
            "day_of_week": obj.get("day_of_week"),
            "day_of_month": obj.get("day_of_month"),
            "month_of_year": obj.get("month_of_year")
        })
        return _obj


