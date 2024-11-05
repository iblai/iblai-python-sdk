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


class RatingEnum(int, Enum):
    """
    * `1` - Up Vote * `-1` - Down Vote
    """

    """
    allowed enum values
    """
    NUMBER_1 = 1
    NUMBER_MINUS_1 = -1

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RatingEnum from a JSON string"""
        return cls(json.loads(json_str))


