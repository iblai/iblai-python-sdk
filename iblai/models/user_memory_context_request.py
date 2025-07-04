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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserMemoryContextRequest(BaseModel):
    """
    UserMemoryContextRequest
    """ # noqa: E501
    extra_data: Optional[StrictStr] = Field(default=None, description="Extra custom data to be added to the memory")
    use_reported_skills: Optional[StrictBool] = None
    use_desired_skills: Optional[StrictBool] = None
    use_credentials: Optional[StrictBool] = None
    use_enrolled_courses: Optional[StrictBool] = None
    use_time_spent: Optional[StrictBool] = None
    use_completed_courses: Optional[StrictBool] = None
    use_completed_programs: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["extra_data", "use_reported_skills", "use_desired_skills", "use_credentials", "use_enrolled_courses", "use_time_spent", "use_completed_courses", "use_completed_programs"]

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
        """Create an instance of UserMemoryContextRequest from a JSON string"""
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
        """Create an instance of UserMemoryContextRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extra_data": obj.get("extra_data"),
            "use_reported_skills": obj.get("use_reported_skills"),
            "use_desired_skills": obj.get("use_desired_skills"),
            "use_credentials": obj.get("use_credentials"),
            "use_enrolled_courses": obj.get("use_enrolled_courses"),
            "use_time_spent": obj.get("use_time_spent"),
            "use_completed_courses": obj.get("use_completed_courses"),
            "use_completed_programs": obj.get("use_completed_programs")
        })
        return _obj


