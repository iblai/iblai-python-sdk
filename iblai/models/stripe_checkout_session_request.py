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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iblai.models.stripe_checkout_session_request_mode_enum import StripeCheckoutSessionRequestModeEnum
from typing import Optional, Set
from typing_extensions import Self

class StripeCheckoutSessionRequest(BaseModel):
    """
    Serializer for Stripe checkout session creation requests.
    """ # noqa: E501
    sku: Optional[StrictStr] = Field(default=None, description="Product SKU")
    product: Optional[StrictStr] = Field(default=None, description="Alternative to SKU")
    success_url: StrictStr = Field(description="URL to redirect after successful payment")
    cancel_url: StrictStr = Field(description="URL to redirect if checkout cancelled")
    mode: Optional[StripeCheckoutSessionRequestModeEnum] = Field(default=None, description="Checkout mode  * `subscription` - subscription * `payment` - payment * `setup` - setup")
    metered: Optional[StrictBool] = Field(default=False, description="Whether to use metered billing")
    quantity: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=1, description="Subscription quantity")
    coupon: Optional[StrictStr] = Field(default=None, description="Coupon code to apply")
    is_free_trial: Optional[StrictBool] = Field(default=False, description="Enable free trial")
    trial_days: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Trial period in days")
    skip_card: Optional[StrictBool] = Field(default=False, description="Skip card collection for trial")
    __properties: ClassVar[List[str]] = ["sku", "product", "success_url", "cancel_url", "mode", "metered", "quantity", "coupon", "is_free_trial", "trial_days", "skip_card"]

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
        """Create an instance of StripeCheckoutSessionRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StripeCheckoutSessionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sku": obj.get("sku"),
            "product": obj.get("product"),
            "success_url": obj.get("success_url"),
            "cancel_url": obj.get("cancel_url"),
            "mode": obj.get("mode"),
            "metered": obj.get("metered") if obj.get("metered") is not None else False,
            "quantity": obj.get("quantity") if obj.get("quantity") is not None else 1,
            "coupon": obj.get("coupon"),
            "is_free_trial": obj.get("is_free_trial") if obj.get("is_free_trial") is not None else False,
            "trial_days": obj.get("trial_days"),
            "skip_card": obj.get("skip_card") if obj.get("skip_card") is not None else False
        })
        return _obj


