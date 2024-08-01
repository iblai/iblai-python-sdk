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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.report_status import ReportStatus
from typing import Optional, Set
from typing_extensions import Self

class ReportData(BaseModel):
    """
    ReportData
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="Report Name")
    description: Optional[StrictStr] = Field(default=None, description="Report Description")
    report_name: Optional[StrictStr] = Field(default=None, description="Report slug")
    icon: Optional[StrictStr] = None
    extra_query_params: Optional[List[Any]] = Field(default=None, description="Extra parameters to be passed to the report create view, e.g learner_id")
    result_columns: Optional[List[Any]] = Field(default=None, description="Columns to be available in the report")
    status: Optional[ReportStatus] = Field(default=None, description="Report Status if any available")
    __properties: ClassVar[List[str]] = ["display_name", "description", "report_name", "icon", "extra_query_params", "result_columns", "status"]

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
        """Create an instance of ReportData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "report_name": obj.get("report_name"),
            "icon": obj.get("icon"),
            "extra_query_params": obj.get("extra_query_params"),
            "result_columns": obj.get("result_columns"),
            "status": ReportStatus.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        return _obj


