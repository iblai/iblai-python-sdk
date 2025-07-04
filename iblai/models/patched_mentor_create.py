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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.greeting_method_enum import GreetingMethodEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedMentorCreate(BaseModel):
    """
    PatchedMentorCreate
    """ # noqa: E501
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    unique_id: Optional[StrictStr] = None
    flow: Optional[Any] = Field(default=None, description="The langflow json for the mentor")
    slug: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    platform: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    allow_anonymous: Optional[StrictBool] = None
    metadata: Optional[Any] = None
    enable_moderation: Optional[StrictBool] = None
    enable_post_processing_system: Optional[StrictBool] = None
    enable_openai_assistant: Optional[StrictBool] = Field(default=None, description="(Deprecated) Set template mentor to openai-agent instead.")
    enable_total_grounding: Optional[StrictBool] = Field(default=None, description="Whether to force mentor to only use information within the provided documents.")
    enable_suggested_prompts: Optional[StrictBool] = Field(default=None, description="Whether to show suggested prompts for the mentor or not. Note: Suggested prompts are created by tenant admins.")
    enable_guided_prompts: Optional[StrictBool] = Field(default=None, description="Whether to show suggested prompts for the mentor or not. Note: Guided prompts are created with an llm based on chat history.")
    google_voice: Optional[StrictInt] = None
    openai_voice: Optional[StrictInt] = None
    guided_prompt_instructions: Optional[StrictStr] = Field(default=None, description="Instructions to determine how prompt suggestions are generated.")
    categories: Optional[List[StrictInt]] = None
    proactive_prompt: Optional[StrictStr] = Field(default=None, description="Prompt template used to start a conversation with the user when greeting_type is proactive_prompt. This will be sent to the LLM so it can respond naturally")
    moderation_system_prompt: Optional[StrictStr] = Field(default=None, description="The prompt for the moderation system. This prompt must clearly distinguish between 'Approapriate' and 'Not Appropriate' queries.")
    post_processing_prompt: Optional[StrictStr] = Field(default=None, description="Prompt to be used to alter or modify final llm response into any desired form.")
    moderation_response: Optional[StrictStr] = Field(default=None, description="Desired feedback to return to the user when their prompt is deemed inappropriate.")
    safety_system_prompt: Optional[StrictStr] = Field(default=None, description="Prompt to check whether the models response is appropriate or not.")
    safety_response: Optional[StrictStr] = Field(default=None, description="Feedback given to the user when a model generates an inappropriate response")
    disable_chathistory: Optional[StrictBool] = None
    enable_safety_system: Optional[StrictBool] = None
    proactive_response: Optional[StrictStr] = Field(default=None, description="Response to start a conversation with a user.")
    mcp_servers: Optional[List[StrictInt]] = None
    greeting_method: Optional[GreetingMethodEnum] = Field(default=None, description="How the mentor should greet the user. proactive_prompt: Allow the LLM to respond to proactive_prompt msg. proactive_response: use proactive_response template without performing an LLM call.  * `proactive_prompt` - Proactive Prompt * `proactive_response` - Proactive Response")
    last_accessed_by: Optional[StrictInt] = Field(default=None, description="edX user ID")
    recently_accessed_at: Optional[datetime] = None
    created_by: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["name", "unique_id", "flow", "slug", "platform", "allow_anonymous", "metadata", "enable_moderation", "enable_post_processing_system", "enable_openai_assistant", "enable_total_grounding", "enable_suggested_prompts", "enable_guided_prompts", "google_voice", "openai_voice", "guided_prompt_instructions", "categories", "proactive_prompt", "moderation_system_prompt", "post_processing_prompt", "moderation_response", "safety_system_prompt", "safety_response", "disable_chathistory", "enable_safety_system", "proactive_response", "mcp_servers", "greeting_method", "last_accessed_by", "recently_accessed_at", "created_by", "created_at", "updated_at"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of PatchedMentorCreate from a JSON string"""
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

        # set to None if google_voice (nullable) is None
        # and model_fields_set contains the field
        if self.google_voice is None and "google_voice" in self.model_fields_set:
            _dict['google_voice'] = None

        # set to None if openai_voice (nullable) is None
        # and model_fields_set contains the field
        if self.openai_voice is None and "openai_voice" in self.model_fields_set:
            _dict['openai_voice'] = None

        # set to None if last_accessed_by (nullable) is None
        # and model_fields_set contains the field
        if self.last_accessed_by is None and "last_accessed_by" in self.model_fields_set:
            _dict['last_accessed_by'] = None

        # set to None if recently_accessed_at (nullable) is None
        # and model_fields_set contains the field
        if self.recently_accessed_at is None and "recently_accessed_at" in self.model_fields_set:
            _dict['recently_accessed_at'] = None

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
        """Create an instance of PatchedMentorCreate from a dict"""
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
            "enable_post_processing_system": obj.get("enable_post_processing_system"),
            "enable_openai_assistant": obj.get("enable_openai_assistant"),
            "enable_total_grounding": obj.get("enable_total_grounding"),
            "enable_suggested_prompts": obj.get("enable_suggested_prompts"),
            "enable_guided_prompts": obj.get("enable_guided_prompts"),
            "google_voice": obj.get("google_voice"),
            "openai_voice": obj.get("openai_voice"),
            "guided_prompt_instructions": obj.get("guided_prompt_instructions"),
            "categories": obj.get("categories"),
            "proactive_prompt": obj.get("proactive_prompt"),
            "moderation_system_prompt": obj.get("moderation_system_prompt"),
            "post_processing_prompt": obj.get("post_processing_prompt"),
            "moderation_response": obj.get("moderation_response"),
            "safety_system_prompt": obj.get("safety_system_prompt"),
            "safety_response": obj.get("safety_response"),
            "disable_chathistory": obj.get("disable_chathistory"),
            "enable_safety_system": obj.get("enable_safety_system"),
            "proactive_response": obj.get("proactive_response"),
            "mcp_servers": obj.get("mcp_servers"),
            "greeting_method": obj.get("greeting_method"),
            "last_accessed_by": obj.get("last_accessed_by"),
            "recently_accessed_at": obj.get("recently_accessed_at"),
            "created_by": obj.get("created_by"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


