# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class VideoEngagementPerCourseData(BaseModel):
    """
    VideoEngagementPerCourseData
    """ # noqa: E501
    name: StrictStr = Field(description="Course name")
    course_id: StrictStr = Field(description="edx Course Id")
    num_vids: StrictInt = Field(description="Number of videos in course")
    num_watched: StrictInt = Field(description="Number of videos watched ")
    time_watched: StrictInt = Field(description="Total time spent by all users watching videos")
    avg_percent_watched: Union[StrictFloat, StrictInt] = Field(description="Average percentage of videos watched per user per course")
    avg_time_watched: Union[StrictFloat, StrictInt] = Field(description="Average time spent per learner")
    __properties: ClassVar[List[str]] = ["name", "course_id", "num_vids", "num_watched", "time_watched", "avg_percent_watched", "avg_time_watched"]

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
        """Create an instance of VideoEngagementPerCourseData from a JSON string"""
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
        """Create an instance of VideoEngagementPerCourseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "course_id": obj.get("course_id"),
            "num_vids": obj.get("num_vids"),
            "num_watched": obj.get("num_watched"),
            "time_watched": obj.get("time_watched"),
            "avg_percent_watched": obj.get("avg_percent_watched"),
            "avg_time_watched": obj.get("avg_time_watched")
        })
        return _obj


