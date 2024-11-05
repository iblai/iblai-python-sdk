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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iblai.models.lti_launch_gate import LtiLaunchGate
from typing import Optional, Set
from typing_extensions import Self

class LtiTool(BaseModel):
    """
    LtiTool
    """ # noqa: E501
    id: StrictInt
    title: StrictStr = Field(description="The title of the tool")
    issuer: StrictStr = Field(description="This value will look someting like https://example.com. Value provided by Lti 1.3 Platform.")
    client_id: StrictStr = Field(description="The client id provided by Lti 1.3 Platform")
    auth_login_url: StrictStr = Field(description="The Platforms OIDC Login endpoint. Value provided by LTI 1.3 Platform.")
    auth_token_url: StrictStr = Field(description="The Platforms OIDC Token endpoint. Value provided by LTI 1.3 Platform.")
    auth_audience: Optional[StrictStr] = Field(default=None, description="The platforms Oauth2 Audience (aud). Usually can be skipped.")
    key_set_url: Optional[StrictStr] = Field(default=None, description="The platforms JWKS endpoint. Value provided by LTI 1.3 Platform.")
    key_set: Optional[Any] = Field(default=None, description="In case Platform's JWKS endpoint is not available, you can provide the JWKS here. Value provided by LTI 1.3 Platform.")
    tool_key: StrictInt = Field(description="Reference to Lti Tool")
    deployment_ids: List[StrictStr] = Field(description="List of deployment ids. Example: [\"1\", \"deployment-2\"]. Value(s) provided by LTI 1.3 Platform.")
    platform_key: StrictStr
    launch_gate: LtiLaunchGate
    __properties: ClassVar[List[str]] = ["id", "title", "issuer", "client_id", "auth_login_url", "auth_token_url", "auth_audience", "key_set_url", "key_set", "tool_key", "deployment_ids", "platform_key", "launch_gate"]

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
        """Create an instance of LtiTool from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of launch_gate
        if self.launch_gate:
            _dict['launch_gate'] = self.launch_gate.to_dict()
        # set to None if auth_audience (nullable) is None
        # and model_fields_set contains the field
        if self.auth_audience is None and "auth_audience" in self.model_fields_set:
            _dict['auth_audience'] = None

        # set to None if key_set_url (nullable) is None
        # and model_fields_set contains the field
        if self.key_set_url is None and "key_set_url" in self.model_fields_set:
            _dict['key_set_url'] = None

        # set to None if key_set (nullable) is None
        # and model_fields_set contains the field
        if self.key_set is None and "key_set" in self.model_fields_set:
            _dict['key_set'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LtiTool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "issuer": obj.get("issuer"),
            "client_id": obj.get("client_id"),
            "auth_login_url": obj.get("auth_login_url"),
            "auth_token_url": obj.get("auth_token_url"),
            "auth_audience": obj.get("auth_audience"),
            "key_set_url": obj.get("key_set_url"),
            "key_set": obj.get("key_set"),
            "tool_key": obj.get("tool_key"),
            "deployment_ids": obj.get("deployment_ids"),
            "platform_key": obj.get("platform_key"),
            "launch_gate": LtiLaunchGate.from_dict(obj["launch_gate"]) if obj.get("launch_gate") is not None else None
        })
        return _obj


