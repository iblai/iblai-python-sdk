# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DataSetStatusEnum(str, Enum):
    """
    * `pending` - Pending * `processing` - Processing * `completed` - Completed * `failed` - Failed
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    FAILED = 'failed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataSetStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


