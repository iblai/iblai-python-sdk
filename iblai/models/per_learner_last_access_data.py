# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.per_learner_course_last_access_data import PerLearnerCourseLastAccessData
from typing import Optional, Set
from typing_extensions import Self

class PerLearnerLastAccessData(BaseModel):
    """
    PerLearnerLastAccessData
    """ # noqa: E501
    course_last_accessed: Optional[PerLearnerCourseLastAccessData] = Field(default=None, description="Course last accessed metadata")
    last_accessed: Optional[StrictStr] = Field(default=None, description="Last accessed time")
    __properties: ClassVar[List[str]] = ["course_last_accessed", "last_accessed"]

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
        """Create an instance of PerLearnerLastAccessData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of course_last_accessed
        if self.course_last_accessed:
            _dict['course_last_accessed'] = self.course_last_accessed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PerLearnerLastAccessData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "course_last_accessed": PerLearnerCourseLastAccessData.from_dict(obj["course_last_accessed"]) if obj.get("course_last_accessed") is not None else None,
            "last_accessed": obj.get("last_accessed")
        })
        return _obj

