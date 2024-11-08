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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from iblai.models.observation import Observation
from typing import Optional, Set
from typing_extensions import Self

class Trace(BaseModel):
    """
    Trace
    """ # noqa: E501
    id: StrictStr
    username: Optional[StrictStr] = None
    external_id: Optional[StrictStr] = Field(alias="externalId")
    timestamp: datetime
    name: StrictStr
    totalprice: Union[StrictFloat, StrictInt]
    user_id: Optional[StrictStr] = Field(alias="userId")
    metadata: Optional[Dict[str, Any]]
    release: Optional[StrictStr]
    version: Optional[StrictStr]
    project_id: StrictStr = Field(alias="projectId")
    public: StrictBool
    bookmarked: StrictBool
    tags: List[StrictStr]
    input: Optional[Any]
    output: Optional[Any]
    session_id: Optional[StrictStr] = Field(alias="sessionId")
    scores: List[Dict[str, Any]]
    observations: List[Observation]
    __properties: ClassVar[List[str]] = ["id", "username", "externalId", "timestamp", "name", "totalprice", "userId", "metadata", "release", "version", "projectId", "public", "bookmarked", "tags", "input", "output", "sessionId", "scores", "observations"]

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
        """Create an instance of Trace from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in observations (list)
        _items = []
        if self.observations:
            for _item in self.observations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['observations'] = _items
        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['externalId'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['userId'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if release (nullable) is None
        # and model_fields_set contains the field
        if self.release is None and "release" in self.model_fields_set:
            _dict['release'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if input (nullable) is None
        # and model_fields_set contains the field
        if self.input is None and "input" in self.model_fields_set:
            _dict['input'] = None

        # set to None if output (nullable) is None
        # and model_fields_set contains the field
        if self.output is None and "output" in self.model_fields_set:
            _dict['output'] = None

        # set to None if session_id (nullable) is None
        # and model_fields_set contains the field
        if self.session_id is None and "session_id" in self.model_fields_set:
            _dict['sessionId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Trace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "externalId": obj.get("externalId"),
            "timestamp": obj.get("timestamp"),
            "name": obj.get("name"),
            "totalprice": obj.get("totalprice"),
            "userId": obj.get("userId"),
            "metadata": obj.get("metadata"),
            "release": obj.get("release"),
            "version": obj.get("version"),
            "projectId": obj.get("projectId"),
            "public": obj.get("public"),
            "bookmarked": obj.get("bookmarked"),
            "tags": obj.get("tags"),
            "input": obj.get("input"),
            "output": obj.get("output"),
            "sessionId": obj.get("sessionId"),
            "scores": obj.get("scores"),
            "observations": [Observation.from_dict(_item) for _item in obj["observations"]] if obj.get("observations") is not None else None
        })
        return _obj


