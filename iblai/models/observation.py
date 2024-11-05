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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Observation(BaseModel):
    """
    Observation
    """ # noqa: E501
    id: StrictStr
    trace_id: StrictStr = Field(alias="traceId")
    project_id: StrictStr = Field(alias="projectId")
    type: StrictStr
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")
    name: StrictStr
    metadata: Optional[Dict[str, Any]]
    parent_observation_id: Optional[StrictStr] = Field(alias="parentObservationId")
    level: StrictStr
    status_message: Optional[StrictStr] = Field(alias="statusMessage")
    version: Optional[StrictStr]
    created_at: datetime = Field(alias="createdAt")
    model: Optional[StrictStr]
    model_parameters: Optional[Dict[str, Any]] = Field(alias="modelParameters")
    input: Optional[Any]
    output: Optional[Any]
    prompt_tokens: StrictInt = Field(alias="promptTokens")
    completion_tokens: StrictInt = Field(alias="completionTokens")
    total_tokens: StrictInt = Field(alias="totalTokens")
    unit: StrictStr
    completion_start_time: Optional[datetime] = Field(alias="completionStartTime")
    prompt_id: Optional[StrictStr] = Field(alias="promptId")
    usage: Optional[Dict[str, Any]] = None
    price: Optional[Union[StrictFloat, StrictInt]]
    __properties: ClassVar[List[str]] = ["id", "traceId", "projectId", "type", "startTime", "endTime", "name", "metadata", "parentObservationId", "level", "statusMessage", "version", "createdAt", "model", "modelParameters", "input", "output", "promptTokens", "completionTokens", "totalTokens", "unit", "completionStartTime", "promptId", "usage", "price"]

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
        """Create an instance of Observation from a JSON string"""
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
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if parent_observation_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_observation_id is None and "parent_observation_id" in self.model_fields_set:
            _dict['parentObservationId'] = None

        # set to None if status_message (nullable) is None
        # and model_fields_set contains the field
        if self.status_message is None and "status_message" in self.model_fields_set:
            _dict['statusMessage'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if model_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.model_parameters is None and "model_parameters" in self.model_fields_set:
            _dict['modelParameters'] = None

        # set to None if input (nullable) is None
        # and model_fields_set contains the field
        if self.input is None and "input" in self.model_fields_set:
            _dict['input'] = None

        # set to None if output (nullable) is None
        # and model_fields_set contains the field
        if self.output is None and "output" in self.model_fields_set:
            _dict['output'] = None

        # set to None if completion_start_time (nullable) is None
        # and model_fields_set contains the field
        if self.completion_start_time is None and "completion_start_time" in self.model_fields_set:
            _dict['completionStartTime'] = None

        # set to None if prompt_id (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_id is None and "prompt_id" in self.model_fields_set:
            _dict['promptId'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Observation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "traceId": obj.get("traceId"),
            "projectId": obj.get("projectId"),
            "type": obj.get("type"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "parentObservationId": obj.get("parentObservationId"),
            "level": obj.get("level"),
            "statusMessage": obj.get("statusMessage"),
            "version": obj.get("version"),
            "createdAt": obj.get("createdAt"),
            "model": obj.get("model"),
            "modelParameters": obj.get("modelParameters"),
            "input": obj.get("input"),
            "output": obj.get("output"),
            "promptTokens": obj.get("promptTokens"),
            "completionTokens": obj.get("completionTokens"),
            "totalTokens": obj.get("totalTokens"),
            "unit": obj.get("unit"),
            "completionStartTime": obj.get("completionStartTime"),
            "promptId": obj.get("promptId"),
            "usage": obj.get("usage"),
            "price": obj.get("price")
        })
        return _obj


