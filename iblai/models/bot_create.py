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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.provider_bd1_enum import ProviderBd1Enum
from typing import Optional, Set
from typing_extensions import Self

class BotCreate(BaseModel):
    """
    BotCreate
    """ # noqa: E501
    id: StrictInt
    name: Annotated[str, Field(strict=True, max_length=255)]
    client_id: Annotated[str, Field(strict=True, max_length=255)]
    client_secret: Annotated[str, Field(strict=True, max_length=500)]
    app_token: Annotated[str, Field(strict=True, max_length=500)]
    verification_token: Annotated[str, Field(strict=True, max_length=500)]
    provider: ProviderBd1Enum
    config: Optional[Any] = None
    webhook_url: StrictStr
    __properties: ClassVar[List[str]] = ["id", "name", "client_id", "client_secret", "app_token", "verification_token", "provider", "config", "webhook_url"]

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
        """Create an instance of BotCreate from a JSON string"""
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
            "id",
            "webhook_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if config (nullable) is None
        # and model_fields_set contains the field
        if self.config is None and "config" in self.model_fields_set:
            _dict['config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BotCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "app_token": obj.get("app_token"),
            "verification_token": obj.get("verification_token"),
            "provider": obj.get("provider"),
            "config": obj.get("config"),
            "webhook_url": obj.get("webhook_url")
        })
        return _obj


