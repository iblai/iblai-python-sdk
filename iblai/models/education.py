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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.institution import Institution
from iblai.models.user_info import UserInfo
from typing import Optional, Set
from typing_extensions import Self

class Education(BaseModel):
    """
    Education
    """ # noqa: E501
    id: StrictInt
    user: StrictInt = Field(description="edX user ID")
    user_info: UserInfo
    institution: Institution
    institution_id: StrictInt
    degree: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    field_of_study: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    start_date: date
    end_date: Optional[date] = None
    grade: Optional[Annotated[str, Field(strict=True)]] = None
    activities: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    description: Optional[StrictStr] = None
    data: Optional[Any] = Field(default=None, description="Metadata")
    metadata: Optional[Any] = Field(default=None, description="Metadata")
    created_at: Optional[datetime] = None
    updated_at: datetime
    is_current: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "user", "user_info", "institution", "institution_id", "degree", "field_of_study", "start_date", "end_date", "grade", "activities", "description", "data", "metadata", "created_at", "updated_at", "is_current"]

    @field_validator('grade')
    def grade_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^-?\d{0,1}(?:\.\d{0,2})?$", value):
            raise ValueError(r"must validate the regular expression /^-?\d{0,1}(?:\.\d{0,2})?$/")
        return value

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
        """Create an instance of Education from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "user",
            "user_info",
            "institution",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user_info
        if self.user_info:
            _dict['user_info'] = self.user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of institution
        if self.institution:
            _dict['institution'] = self.institution.to_dict()
        # set to None if degree (nullable) is None
        # and model_fields_set contains the field
        if self.degree is None and "degree" in self.model_fields_set:
            _dict['degree'] = None

        # set to None if field_of_study (nullable) is None
        # and model_fields_set contains the field
        if self.field_of_study is None and "field_of_study" in self.model_fields_set:
            _dict['field_of_study'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['end_date'] = None

        # set to None if grade (nullable) is None
        # and model_fields_set contains the field
        if self.grade is None and "grade" in self.model_fields_set:
            _dict['grade'] = None

        # set to None if activities (nullable) is None
        # and model_fields_set contains the field
        if self.activities is None and "activities" in self.model_fields_set:
            _dict['activities'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if is_current (nullable) is None
        # and model_fields_set contains the field
        if self.is_current is None and "is_current" in self.model_fields_set:
            _dict['is_current'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Education from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user": obj.get("user"),
            "user_info": UserInfo.from_dict(obj["user_info"]) if obj.get("user_info") is not None else None,
            "institution": Institution.from_dict(obj["institution"]) if obj.get("institution") is not None else None,
            "institution_id": obj.get("institution_id"),
            "degree": obj.get("degree"),
            "field_of_study": obj.get("field_of_study"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "grade": obj.get("grade"),
            "activities": obj.get("activities"),
            "description": obj.get("description"),
            "data": obj.get("data"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "is_current": obj.get("is_current")
        })
        return _obj


