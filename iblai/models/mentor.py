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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Mentor(BaseModel):
    """
    Mentor
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=255)]
    unique_id: Optional[StrictStr] = None
    flow: Optional[Any] = Field(description="The langflow json for the mentor")
    slug: Annotated[str, Field(strict=True, max_length=255)]
    platform: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    allow_anonymous: Optional[StrictBool] = None
    metadata: Optional[Any] = None
    enable_moderation: Optional[StrictBool] = None
    is_proactive: Optional[StrictBool] = Field(default=None, description="If true, the mentor will be prompted to start a conversation with a user.")
    proactive_prompt: Optional[StrictStr] = Field(default=None, description="Prompt to start a conversation with a user. This prompt will be fed to the mentor as soon as the user enters the chatroom. This is used if is_proactive is true.")
    moderation_system_prompt: Optional[StrictStr] = Field(default=None, description="The prompt for the moderation system. This prompt must clearly distinguish between 'Approapriate' and 'Not Appropriate' queries.")
    moderation_response: Optional[StrictStr] = Field(default=None, description="Desired feedback to return to the user when their prompt is deemed inappropriate.")
    safety_system_prompt: Optional[StrictStr] = Field(default=None, description="Prompt to check whether the models response is appropriate or not.")
    safety_response: Optional[StrictStr] = Field(default=None, description="Feedback given to the user when a model generates an inappropriate response")
    enable_safety_system: Optional[StrictBool] = None
    proactive_message: Optional[StrictStr] = Field(default=None, description="Prompt to start a conversation with a user.")
    created_by: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    __properties: ClassVar[List[str]] = ["name", "unique_id", "flow", "slug", "platform", "allow_anonymous", "metadata", "enable_moderation", "is_proactive", "proactive_prompt", "moderation_system_prompt", "moderation_response", "safety_system_prompt", "safety_response", "enable_safety_system", "proactive_message", "created_by", "created_at", "updated_at"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
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
        """Create an instance of Mentor from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if flow (nullable) is None
        # and model_fields_set contains the field
        if self.flow is None and "flow" in self.model_fields_set:
            _dict['flow'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if proactive_message (nullable) is None
        # and model_fields_set contains the field
        if self.proactive_message is None and "proactive_message" in self.model_fields_set:
            _dict['proactive_message'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Mentor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "unique_id": obj.get("unique_id"),
            "flow": obj.get("flow"),
            "slug": obj.get("slug"),
            "platform": obj.get("platform"),
            "allow_anonymous": obj.get("allow_anonymous"),
            "metadata": obj.get("metadata"),
            "enable_moderation": obj.get("enable_moderation"),
            "is_proactive": obj.get("is_proactive"),
            "proactive_prompt": obj.get("proactive_prompt"),
            "moderation_system_prompt": obj.get("moderation_system_prompt"),
            "moderation_response": obj.get("moderation_response"),
            "safety_system_prompt": obj.get("safety_system_prompt"),
            "safety_response": obj.get("safety_response"),
            "enable_safety_system": obj.get("enable_safety_system"),
            "proactive_message": obj.get("proactive_message"),
            "created_by": obj.get("created_by"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


