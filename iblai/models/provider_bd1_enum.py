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


class ProviderBd1Enum(str, Enum):
    """
    * `webex` - Webex * `slack` - Slack * `whatsapp` - Whatsapp * `discord` - Discord
    """

    """
    allowed enum values
    """
    WEBEX = 'webex'
    SLACK = 'slack'
    WHATSAPP = 'whatsapp'
    DISCORD = 'discord'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProviderBd1Enum from a JSON string"""
        return cls(json.loads(json_str))


