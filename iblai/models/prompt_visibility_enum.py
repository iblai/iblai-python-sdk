# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PromptVisibilityEnum(str, Enum):
    """
    * `viewable_by_tenant_admins` - Viewable By Tenant Admins * `viewable_by_tenant_students` - Viewable By Tenant Students * `viewable_by_anyone` - Viewable By Anyone
    """

    """
    allowed enum values
    """
    VIEWABLE_BY_TENANT_ADMINS = 'viewable_by_tenant_admins'
    VIEWABLE_BY_TENANT_STUDENTS = 'viewable_by_tenant_students'
    VIEWABLE_BY_ANYONE = 'viewable_by_anyone'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PromptVisibilityEnum from a JSON string"""
        return cls(json.loads(json_str))


