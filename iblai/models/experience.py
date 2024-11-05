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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.company import Company
from iblai.models.user_info import UserInfo
from typing import Optional, Set
from typing_extensions import Self

class Experience(BaseModel):
    """
    Experience
    """ # noqa: E501
    id: StrictInt
    user: StrictInt = Field(description="edX user ID")
    user_info: UserInfo
    company: Company
    company_id: StrictInt
    title: Annotated[str, Field(strict=True, max_length=100)]
    employment_type: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    location: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    start_date: date
    end_date: Optional[date] = None
    is_current: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    data: Optional[Any] = Field(default=None, description="Metadata")
    metadata: Optional[Any] = Field(default=None, description="Metadata")
    created_at: Optional[datetime] = None
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["id", "user", "user_info", "company", "company_id", "title", "employment_type", "location", "start_date", "end_date", "is_current", "description", "data", "metadata", "created_at", "updated_at"]

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
        """Create an instance of Experience from a JSON string"""
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
            "company",
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
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # set to None if employment_type (nullable) is None
        # and model_fields_set contains the field
        if self.employment_type is None and "employment_type" in self.model_fields_set:
            _dict['employment_type'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['end_date'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Experience from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "user": obj.get("user"),
            "user_info": UserInfo.from_dict(obj["user_info"]) if obj.get("user_info") is not None else None,
            "company": Company.from_dict(obj["company"]) if obj.get("company") is not None else None,
            "company_id": obj.get("company_id"),
            "title": obj.get("title"),
            "employment_type": obj.get("employment_type"),
            "location": obj.get("location"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "is_current": obj.get("is_current"),
            "description": obj.get("description"),
            "data": obj.get("data"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


