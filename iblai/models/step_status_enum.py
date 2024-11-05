# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StepStatusEnum(str, Enum):
    """
    * `completed` - Completed * `failed` - Failed * `pending` - Pending
    """

    """
    allowed enum values
    """
    COMPLETED = 'completed'
    FAILED = 'failed'
    PENDING = 'pending'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StepStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


