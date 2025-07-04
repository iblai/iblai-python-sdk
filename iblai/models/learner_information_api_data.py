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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LearnerInformationAPIData(BaseModel):
    """
    LearnerInformationAPIData
    """ # noqa: E501
    username: StrictStr = Field(description="learner username")
    name: StrictStr = Field(description="learner Name")
    email: StrictStr = Field(description="learner email")
    date_joined: StrictStr = Field(description="Registration Timestamp e.g 2022-05-05T00:00:00+00:00")
    last_activity: StrictStr = Field(description="Last Activity Timestamp e.g 2022-05-05T00:00:00+00:00")
    total_assessments: Optional[StrictInt] = Field(default=None, description="Total assessments attempted")
    total_time_spent: Optional[StrictInt] = Field(default=None, description="Total time spent in seconds")
    total_videos: Optional[StrictInt] = Field(default=None, description="Total videos watched")
    course_completions: Optional[StrictInt] = Field(default=None, description="Total courses completed")
    time_spent_overtime: Optional[Dict[str, Any]] = None
    continent: Optional[StrictStr] = Field(default=None, description="last location - continent")
    continent_code: Optional[StrictStr] = Field(default=None, description="last location - continent code")
    country: Optional[StrictStr] = Field(default=None, description="last location - country")
    country_code: Optional[StrictStr] = Field(default=None, description="last location - country code")
    region: Optional[StrictStr] = Field(default=None, description="last location - region")
    region_code: Optional[StrictStr] = Field(default=None, description="last location - region code")
    location: Optional[StrictStr] = Field(default=None, description="last location")
    city: Optional[StrictStr] = Field(default=None, description="last location - city")
    browser: Optional[StrictStr] = Field(default=None, description="last known browser")
    operating_system: Optional[StrictStr] = Field(default=None, description="last known operating system")
    resolution: Optional[StrictStr] = Field(default=None, description="last known browser resolution")
    __properties: ClassVar[List[str]] = ["username", "name", "email", "date_joined", "last_activity", "total_assessments", "total_time_spent", "total_videos", "course_completions", "time_spent_overtime", "continent", "continent_code", "country", "country_code", "region", "region_code", "location", "city", "browser", "operating_system", "resolution"]

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
        """Create an instance of LearnerInformationAPIData from a JSON string"""
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
        """Create an instance of LearnerInformationAPIData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "username": obj.get("username"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "date_joined": obj.get("date_joined"),
            "last_activity": obj.get("last_activity"),
            "total_assessments": obj.get("total_assessments"),
            "total_time_spent": obj.get("total_time_spent"),
            "total_videos": obj.get("total_videos"),
            "course_completions": obj.get("course_completions"),
            "time_spent_overtime": obj.get("time_spent_overtime"),
            "continent": obj.get("continent"),
            "continent_code": obj.get("continent_code"),
            "country": obj.get("country"),
            "country_code": obj.get("country_code"),
            "region": obj.get("region"),
            "region_code": obj.get("region_code"),
            "location": obj.get("location"),
            "city": obj.get("city"),
            "browser": obj.get("browser"),
            "operating_system": obj.get("operating_system"),
            "resolution": obj.get("resolution")
        })
        return _obj


