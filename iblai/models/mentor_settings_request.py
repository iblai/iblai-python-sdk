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

class MentorSettingsRequest(BaseModel):
    """
    MentorSettingsRequest
    """ # noqa: E501
    mentor_name: Optional[StrictStr] = None
    template_name: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    profile_image: Optional[StrictStr] = None
    initial_message: Optional[StrictStr] = None
    suggested_message: Optional[StrictStr] = None
    theme: Optional[StrictStr] = None
    user_message_color: Optional[StrictStr] = None
    mentor_bubble_color: Optional[StrictStr] = None
    align_mentor_bubble: Optional[StrictStr] = None
    system_prompt: Optional[StrictStr] = None
    llm_provider: Optional[StrictStr] = None
    llm_name: Optional[StrictStr] = None
    featured: Optional[StrictBool] = None
    disable_chathistory: Optional[StrictBool] = None
    metadata: Optional[Any] = None
    custom_css: Optional[StrictStr] = None
    department_id: Optional[StrictInt] = Field(default=None, description="Department to authorize users by")
    mentor_visibility: Optional[StrictStr] = None
    enable_image_generation: Optional[StrictBool] = None
    enable_web_browsing: Optional[StrictBool] = None
    enable_code_interpreter: Optional[StrictBool] = None
    allow_anonymous: Optional[StrictBool] = None
    forkable: Optional[StrictBool] = None
    forkable_with_training_data: Optional[StrictBool] = None
    mentor_description: Optional[StrictStr] = None
    uploaded_profile_image: Optional[StrictStr] = None
    proactive_response: Optional[StrictStr] = None
    greeting_method: Optional[GreetingMethodEnum] = None
    can_use_tools: Optional[StrictBool] = None
    tool_slugs: Optional[List[StrictStr]] = None
    llm_temperature: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = None
    proactive_prompt: Optional[StrictStr] = None
    moderation_system_prompt: Optional[StrictStr] = None
    post_processing_prompt: Optional[StrictStr] = None
    moderation_response: Optional[StrictStr] = None
    enable_moderation: Optional[StrictBool] = None
    enable_post_processing_system: Optional[StrictBool] = None
    enable_openai_assistant: Optional[StrictBool] = None
    enable_total_grounding: Optional[StrictBool] = None
    enable_suggested_prompts: Optional[StrictBool] = None
    enable_guided_prompts: Optional[StrictBool] = None
    mcp_servers: Optional[List[StrictInt]] = None
    google_voice: Optional[StrictInt] = None
    openai_voice: Optional[StrictInt] = None
    guided_prompt_instructions: Optional[StrictStr] = None
    safety_system_prompt: Optional[StrictStr] = None
    safety_response: Optional[StrictStr] = None
    enable_safety_system: Optional[StrictBool] = None
    enable_memory_component: Optional[StrictBool] = False
    enable_spaced_repetition: Optional[StrictBool] = False
    enable_instruction_mode: Optional[StrictBool] = False
    enable_socratic_mode: Optional[StrictBool] = False
    is_guided_mentor: Optional[StrictBool] = False
    enable_email_chat: Optional[StrictBool] = False
    categories: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["mentor_name", "template_name", "display_name", "profile_image", "initial_message", "suggested_message", "theme", "user_message_color", "mentor_bubble_color", "align_mentor_bubble", "system_prompt", "llm_provider", "llm_name", "featured", "disable_chathistory", "metadata", "custom_css", "department_id", "mentor_visibility", "enable_image_generation", "enable_web_browsing", "enable_code_interpreter", "allow_anonymous", "forkable", "forkable_with_training_data", "mentor_description", "uploaded_profile_image", "proactive_response", "greeting_method", "can_use_tools", "tool_slugs", "llm_temperature", "proactive_prompt", "moderation_system_prompt", "post_processing_prompt", "moderation_response", "enable_moderation", "enable_post_processing_system", "enable_openai_assistant", "enable_total_grounding", "enable_suggested_prompts", "enable_guided_prompts", "mcp_servers", "google_voice", "openai_voice", "guided_prompt_instructions", "safety_system_prompt", "safety_response", "enable_safety_system", "enable_memory_component", "enable_spaced_repetition", "enable_instruction_mode", "enable_socratic_mode", "is_guided_mentor", "enable_email_chat", "categories"]

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
        """Create an instance of MentorSettingsRequest from a JSON string"""
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
        # set to None if initial_message (nullable) is None
        # and model_fields_set contains the field
        if self.initial_message is None and "initial_message" in self.model_fields_set:
            _dict['initial_message'] = None

        # set to None if suggested_message (nullable) is None
        # and model_fields_set contains the field
        if self.suggested_message is None and "suggested_message" in self.model_fields_set:
            _dict['suggested_message'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if custom_css (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css is None and "custom_css" in self.model_fields_set:
            _dict['custom_css'] = None

        # set to None if department_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_id is None and "department_id" in self.model_fields_set:
            _dict['department_id'] = None

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
        """Create an instance of MentorSettingsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mentor_name": obj.get("mentor_name"),
            "template_name": obj.get("template_name"),
            "display_name": obj.get("display_name"),
            "profile_image": obj.get("profile_image"),
            "initial_message": obj.get("initial_message"),
            "suggested_message": obj.get("suggested_message"),
            "theme": obj.get("theme"),
            "user_message_color": obj.get("user_message_color"),
            "mentor_bubble_color": obj.get("mentor_bubble_color"),
            "align_mentor_bubble": obj.get("align_mentor_bubble"),
            "system_prompt": obj.get("system_prompt"),
            "llm_provider": obj.get("llm_provider"),
            "llm_name": obj.get("llm_name"),
            "featured": obj.get("featured"),
            "disable_chathistory": obj.get("disable_chathistory"),
            "metadata": obj.get("metadata"),
            "custom_css": obj.get("custom_css"),
            "department_id": obj.get("department_id"),
            "mentor_visibility": obj.get("mentor_visibility"),
            "enable_image_generation": obj.get("enable_image_generation"),
            "enable_web_browsing": obj.get("enable_web_browsing"),
            "enable_code_interpreter": obj.get("enable_code_interpreter"),
            "allow_anonymous": obj.get("allow_anonymous"),
            "forkable": obj.get("forkable"),
            "forkable_with_training_data": obj.get("forkable_with_training_data"),
            "mentor_description": obj.get("mentor_description"),
            "uploaded_profile_image": obj.get("uploaded_profile_image"),
            "proactive_response": obj.get("proactive_response"),
            "greeting_method": obj.get("greeting_method"),
            "can_use_tools": obj.get("can_use_tools"),
            "tool_slugs": obj.get("tool_slugs"),
            "llm_temperature": obj.get("llm_temperature"),
            "proactive_prompt": obj.get("proactive_prompt"),
            "moderation_system_prompt": obj.get("moderation_system_prompt"),
            "post_processing_prompt": obj.get("post_processing_prompt"),
            "moderation_response": obj.get("moderation_response"),
            "enable_moderation": obj.get("enable_moderation"),
            "enable_post_processing_system": obj.get("enable_post_processing_system"),
            "enable_openai_assistant": obj.get("enable_openai_assistant"),
            "enable_total_grounding": obj.get("enable_total_grounding"),
            "enable_suggested_prompts": obj.get("enable_suggested_prompts"),
            "enable_guided_prompts": obj.get("enable_guided_prompts"),
            "mcp_servers": obj.get("mcp_servers"),
            "google_voice": obj.get("google_voice"),
            "openai_voice": obj.get("openai_voice"),
            "guided_prompt_instructions": obj.get("guided_prompt_instructions"),
            "safety_system_prompt": obj.get("safety_system_prompt"),
            "safety_response": obj.get("safety_response"),
            "enable_safety_system": obj.get("enable_safety_system"),
            "enable_memory_component": obj.get("enable_memory_component") if obj.get("enable_memory_component") is not None else False,
            "enable_spaced_repetition": obj.get("enable_spaced_repetition") if obj.get("enable_spaced_repetition") is not None else False,
            "enable_instruction_mode": obj.get("enable_instruction_mode") if obj.get("enable_instruction_mode") is not None else False,
            "enable_socratic_mode": obj.get("enable_socratic_mode") if obj.get("enable_socratic_mode") is not None else False,
            "is_guided_mentor": obj.get("is_guided_mentor") if obj.get("is_guided_mentor") is not None else False,
            "enable_email_chat": obj.get("enable_email_chat") if obj.get("enable_email_chat") is not None else False,
            "categories": obj.get("categories")
        })
        return _obj


