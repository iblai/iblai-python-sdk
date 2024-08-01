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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MentorFromTemplateWithSettingRequest(BaseModel):
    """
    MentorFromTemplateWithSettingRequest
    """ # noqa: E501
    template_name: StrictStr
    display_name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    profile_image: Optional[StrictStr] = None
    initial_message: Optional[StrictStr] = None
    suggested_message: Optional[StrictStr] = None
    new_mentor_name: StrictStr
    theme: Optional[StrictStr] = None
    user_message_color: Optional[StrictStr] = None
    mentor_bubble_color: Optional[StrictStr] = None
    align_mentor_bubble: Optional[StrictStr] = None
    system_prompt: Optional[StrictStr] = None
    llm_provider: Optional[StrictStr] = None
    llm_name: Optional[StrictStr] = None
    mentor_visibility: Optional[StrictStr] = None
    enable_image_generation: Optional[StrictBool] = None
    enable_web_browsing: Optional[StrictBool] = None
    enable_code_interpreter: Optional[StrictBool] = None
    metadata: Optional[Any] = None
    custom_css: Optional[StrictStr] = None
    uploaded_profile_image: Optional[StrictStr] = None
    proactive_message: Optional[StrictStr] = None
    tool_slugs: Optional[List[StrictStr]] = None
    llm_temperature: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = None
    seo_tags: Optional[Any] = None
    marketing_conversations: Optional[Any] = None
    proactive_prompt: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["template_name", "display_name", "description", "profile_image", "initial_message", "suggested_message", "new_mentor_name", "theme", "user_message_color", "mentor_bubble_color", "align_mentor_bubble", "system_prompt", "llm_provider", "llm_name", "mentor_visibility", "enable_image_generation", "enable_web_browsing", "enable_code_interpreter", "metadata", "custom_css", "uploaded_profile_image", "proactive_message", "tool_slugs", "llm_temperature", "seo_tags", "marketing_conversations", "proactive_prompt"]

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
        """Create an instance of MentorFromTemplateWithSettingRequest from a JSON string"""
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

        # set to None if seo_tags (nullable) is None
        # and model_fields_set contains the field
        if self.seo_tags is None and "seo_tags" in self.model_fields_set:
            _dict['seo_tags'] = None

        # set to None if marketing_conversations (nullable) is None
        # and model_fields_set contains the field
        if self.marketing_conversations is None and "marketing_conversations" in self.model_fields_set:
            _dict['marketing_conversations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MentorFromTemplateWithSettingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "template_name": obj.get("template_name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "profile_image": obj.get("profile_image"),
            "initial_message": obj.get("initial_message"),
            "suggested_message": obj.get("suggested_message"),
            "new_mentor_name": obj.get("new_mentor_name"),
            "theme": obj.get("theme"),
            "user_message_color": obj.get("user_message_color"),
            "mentor_bubble_color": obj.get("mentor_bubble_color"),
            "align_mentor_bubble": obj.get("align_mentor_bubble"),
            "system_prompt": obj.get("system_prompt"),
            "llm_provider": obj.get("llm_provider"),
            "llm_name": obj.get("llm_name"),
            "mentor_visibility": obj.get("mentor_visibility"),
            "enable_image_generation": obj.get("enable_image_generation"),
            "enable_web_browsing": obj.get("enable_web_browsing"),
            "enable_code_interpreter": obj.get("enable_code_interpreter"),
            "metadata": obj.get("metadata"),
            "custom_css": obj.get("custom_css"),
            "uploaded_profile_image": obj.get("uploaded_profile_image"),
            "proactive_message": obj.get("proactive_message"),
            "tool_slugs": obj.get("tool_slugs"),
            "llm_temperature": obj.get("llm_temperature"),
            "seo_tags": obj.get("seo_tags"),
            "marketing_conversations": obj.get("marketing_conversations"),
            "proactive_prompt": obj.get("proactive_prompt")
        })
        return _obj


