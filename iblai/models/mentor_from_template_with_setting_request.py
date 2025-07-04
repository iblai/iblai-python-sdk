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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from iblai.models.greeting_method_enum import GreetingMethodEnum
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
    proactive_response: Optional[StrictStr] = None
    greeting_method: Optional[GreetingMethodEnum] = None
    forkable: Optional[StrictBool] = None
    forkable_with_training_data: Optional[StrictBool] = None
    categories: Optional[List[StrictInt]] = None
    tool_slugs: Optional[List[StrictStr]] = None
    llm_temperature: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = None
    seo_tags: Optional[Any] = None
    marketing_conversations: Optional[Any] = None
    proactive_prompt: Optional[StrictStr] = None
    moderation_system_prompt: Optional[StrictStr] = None
    post_processing_prompt: Optional[StrictStr] = None
    moderation_response: Optional[StrictStr] = None
    enable_moderation: Optional[StrictBool] = False
    enable_post_processing_system: Optional[StrictBool] = False
    enable_openai_assistant: Optional[StrictBool] = None
    enable_total_grounding: Optional[StrictBool] = False
    google_voice: Optional[StrictInt] = None
    openai_voice: Optional[StrictInt] = None
    enable_suggested_prompts: Optional[StrictBool] = None
    enable_guided_prompts: Optional[StrictBool] = None
    mcp_servers: Optional[List[StrictInt]] = None
    guided_prompt_instructions: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["template_name", "display_name", "description", "profile_image", "initial_message", "suggested_message", "new_mentor_name", "theme", "user_message_color", "mentor_bubble_color", "align_mentor_bubble", "system_prompt", "llm_provider", "llm_name", "mentor_visibility", "enable_image_generation", "enable_web_browsing", "enable_code_interpreter", "metadata", "custom_css", "uploaded_profile_image", "proactive_response", "greeting_method", "forkable", "forkable_with_training_data", "categories", "tool_slugs", "llm_temperature", "seo_tags", "marketing_conversations", "proactive_prompt", "moderation_system_prompt", "post_processing_prompt", "moderation_response", "enable_moderation", "enable_post_processing_system", "enable_openai_assistant", "enable_total_grounding", "google_voice", "openai_voice", "enable_suggested_prompts", "enable_guided_prompts", "mcp_servers", "guided_prompt_instructions"]

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

        # set to None if enable_suggested_prompts (nullable) is None
        # and model_fields_set contains the field
        if self.enable_suggested_prompts is None and "enable_suggested_prompts" in self.model_fields_set:
            _dict['enable_suggested_prompts'] = None

        # set to None if enable_guided_prompts (nullable) is None
        # and model_fields_set contains the field
        if self.enable_guided_prompts is None and "enable_guided_prompts" in self.model_fields_set:
            _dict['enable_guided_prompts'] = None

        # set to None if mcp_servers (nullable) is None
        # and model_fields_set contains the field
        if self.mcp_servers is None and "mcp_servers" in self.model_fields_set:
            _dict['mcp_servers'] = None

        # set to None if guided_prompt_instructions (nullable) is None
        # and model_fields_set contains the field
        if self.guided_prompt_instructions is None and "guided_prompt_instructions" in self.model_fields_set:
            _dict['guided_prompt_instructions'] = None

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
            "proactive_response": obj.get("proactive_response"),
            "greeting_method": obj.get("greeting_method"),
            "forkable": obj.get("forkable"),
            "forkable_with_training_data": obj.get("forkable_with_training_data"),
            "categories": obj.get("categories"),
            "tool_slugs": obj.get("tool_slugs"),
            "llm_temperature": obj.get("llm_temperature"),
            "seo_tags": obj.get("seo_tags"),
            "marketing_conversations": obj.get("marketing_conversations"),
            "proactive_prompt": obj.get("proactive_prompt"),
            "moderation_system_prompt": obj.get("moderation_system_prompt"),
            "post_processing_prompt": obj.get("post_processing_prompt"),
            "moderation_response": obj.get("moderation_response"),
            "enable_moderation": obj.get("enable_moderation") if obj.get("enable_moderation") is not None else False,
            "enable_post_processing_system": obj.get("enable_post_processing_system") if obj.get("enable_post_processing_system") is not None else False,
            "enable_openai_assistant": obj.get("enable_openai_assistant"),
            "enable_total_grounding": obj.get("enable_total_grounding") if obj.get("enable_total_grounding") is not None else False,
            "google_voice": obj.get("google_voice"),
            "openai_voice": obj.get("openai_voice"),
            "enable_suggested_prompts": obj.get("enable_suggested_prompts"),
            "enable_guided_prompts": obj.get("enable_guided_prompts"),
            "mcp_servers": obj.get("mcp_servers"),
            "guided_prompt_instructions": obj.get("guided_prompt_instructions")
        })
        return _obj


