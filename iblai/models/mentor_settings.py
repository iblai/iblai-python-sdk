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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.align_mentor_bubble_enum import AlignMentorBubbleEnum
from iblai.models.mentor_settings_mentor_visibility import MentorSettingsMentorVisibility
from iblai.models.theme_enum import ThemeEnum
from typing import Optional, Set
from typing_extensions import Self

class MentorSettings(BaseModel):
    """
    MentorSettings
    """ # noqa: E501
    id: StrictInt
    display_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    profile_image: Optional[StrictStr] = None
    initial_message: Optional[StrictStr] = None
    suggested_message: Optional[StrictStr] = None
    theme: Optional[ThemeEnum] = None
    user_message_color: Optional[Annotated[str, Field(strict=True, max_length=7)]] = None
    mentor_bubble_color: Optional[Annotated[str, Field(strict=True, max_length=7)]] = None
    align_mentor_bubble: Optional[AlignMentorBubbleEnum] = None
    mentor: StrictStr
    mentor_slug: StrictStr
    mentor_unique_id: StrictStr
    metadata: StrictStr
    mentor_visibility: Optional[MentorSettingsMentorVisibility] = None
    enable_image_generation: Optional[StrictBool] = None
    enable_web_browsing: Optional[StrictBool] = None
    enable_code_interpreter: Optional[StrictBool] = None
    custom_css: Optional[StrictStr] = None
    allow_anonymous: StrictStr
    mentor_description: StrictStr
    suggested_prompts: StrictStr
    proactive_message: StrictStr
    mentor_tools: StrictStr
    can_use_tools: StrictStr
    llm_temperature: StrictStr
    llm_provider: StrictStr
    llm_name: StrictStr
    proactive_prompt: StrictStr
    __properties: ClassVar[List[str]] = ["id", "display_name", "profile_image", "initial_message", "suggested_message", "theme", "user_message_color", "mentor_bubble_color", "align_mentor_bubble", "mentor", "mentor_slug", "mentor_unique_id", "metadata", "mentor_visibility", "enable_image_generation", "enable_web_browsing", "enable_code_interpreter", "custom_css", "allow_anonymous", "mentor_description", "suggested_prompts", "proactive_message", "mentor_tools", "can_use_tools", "llm_temperature", "llm_provider", "llm_name", "proactive_prompt"]

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
        """Create an instance of MentorSettings from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "mentor",
            "mentor_slug",
            "mentor_unique_id",
            "metadata",
            "allow_anonymous",
            "mentor_description",
            "suggested_prompts",
            "proactive_message",
            "mentor_tools",
            "can_use_tools",
            "llm_temperature",
            "llm_provider",
            "llm_name",
            "proactive_prompt",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of mentor_visibility
        if self.mentor_visibility:
            _dict['mentor_visibility'] = self.mentor_visibility.to_dict()
        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

        # set to None if profile_image (nullable) is None
        # and model_fields_set contains the field
        if self.profile_image is None and "profile_image" in self.model_fields_set:
            _dict['profile_image'] = None

        # set to None if initial_message (nullable) is None
        # and model_fields_set contains the field
        if self.initial_message is None and "initial_message" in self.model_fields_set:
            _dict['initial_message'] = None

        # set to None if suggested_message (nullable) is None
        # and model_fields_set contains the field
        if self.suggested_message is None and "suggested_message" in self.model_fields_set:
            _dict['suggested_message'] = None

        # set to None if mentor_visibility (nullable) is None
        # and model_fields_set contains the field
        if self.mentor_visibility is None and "mentor_visibility" in self.model_fields_set:
            _dict['mentor_visibility'] = None

        # set to None if enable_image_generation (nullable) is None
        # and model_fields_set contains the field
        if self.enable_image_generation is None and "enable_image_generation" in self.model_fields_set:
            _dict['enable_image_generation'] = None

        # set to None if enable_web_browsing (nullable) is None
        # and model_fields_set contains the field
        if self.enable_web_browsing is None and "enable_web_browsing" in self.model_fields_set:
            _dict['enable_web_browsing'] = None

        # set to None if enable_code_interpreter (nullable) is None
        # and model_fields_set contains the field
        if self.enable_code_interpreter is None and "enable_code_interpreter" in self.model_fields_set:
            _dict['enable_code_interpreter'] = None

        # set to None if custom_css (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css is None and "custom_css" in self.model_fields_set:
            _dict['custom_css'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MentorSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "display_name": obj.get("display_name"),
            "profile_image": obj.get("profile_image"),
            "initial_message": obj.get("initial_message"),
            "suggested_message": obj.get("suggested_message"),
            "theme": obj.get("theme"),
            "user_message_color": obj.get("user_message_color"),
            "mentor_bubble_color": obj.get("mentor_bubble_color"),
            "align_mentor_bubble": obj.get("align_mentor_bubble"),
            "mentor": obj.get("mentor"),
            "mentor_slug": obj.get("mentor_slug"),
            "mentor_unique_id": obj.get("mentor_unique_id"),
            "metadata": obj.get("metadata"),
            "mentor_visibility": MentorSettingsMentorVisibility.from_dict(obj["mentor_visibility"]) if obj.get("mentor_visibility") is not None else None,
            "enable_image_generation": obj.get("enable_image_generation"),
            "enable_web_browsing": obj.get("enable_web_browsing"),
            "enable_code_interpreter": obj.get("enable_code_interpreter"),
            "custom_css": obj.get("custom_css"),
            "allow_anonymous": obj.get("allow_anonymous"),
            "mentor_description": obj.get("mentor_description"),
            "suggested_prompts": obj.get("suggested_prompts"),
            "proactive_message": obj.get("proactive_message"),
            "mentor_tools": obj.get("mentor_tools"),
            "can_use_tools": obj.get("can_use_tools"),
            "llm_temperature": obj.get("llm_temperature"),
            "llm_provider": obj.get("llm_provider"),
            "llm_name": obj.get("llm_name"),
            "proactive_prompt": obj.get("proactive_prompt")
        })
        return _obj


