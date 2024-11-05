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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from iblai.models.data_set import DataSet
from iblai.models.provider63a_enum import Provider63aEnum
from iblai.models.training_status_enum import TrainingStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class Training(BaseModel):
    """
    Training
    """ # noqa: E501
    id: Optional[StrictStr] = None
    dataset: DataSet
    project_name: Annotated[str, Field(strict=True, max_length=255)]
    metadata: Optional[Any] = None
    status: Optional[TrainingStatusEnum] = None
    retry_attempts: Optional[StrictInt] = None
    fine_tuned_model: Optional[Annotated[str, Field(strict=True, max_length=400)]] = None
    provider: Optional[Provider63aEnum] = None
    base_model_name: Annotated[str, Field(strict=True, max_length=400)]
    text_column: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    learning_rate: Optional[Union[StrictFloat, StrictInt]] = None
    batch_size: Optional[StrictInt] = None
    num_epochs: Optional[StrictInt] = None
    block_size: Optional[StrictInt] = None
    warmup_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    lora_r: Optional[StrictInt] = None
    lora_alpha: Optional[StrictInt] = None
    lora_dropout: Optional[Union[StrictFloat, StrictInt]] = None
    weight_decay: Optional[Union[StrictFloat, StrictInt]] = None
    gradient_accumulation: Optional[StrictInt] = None
    use_peft: Optional[StrictBool] = None
    use_fp16: Optional[StrictBool] = None
    use_int4: Optional[StrictBool] = None
    push_to_hub: Optional[StrictBool] = None
    repo_id: Optional[Annotated[str, Field(strict=True, max_length=400)]] = None
    preprocess_dataset: Optional[StrictBool] = None
    prompt_column: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    response_column: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    prompt_prefix: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    prompt_suffix: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    response_prefix: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    response_suffix: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    error_log: Optional[StrictStr] = None
    date_created: datetime
    last_modified: datetime
    platform: StrictInt
    __properties: ClassVar[List[str]] = ["id", "dataset", "project_name", "metadata", "status", "retry_attempts", "fine_tuned_model", "provider", "base_model_name", "text_column", "learning_rate", "batch_size", "num_epochs", "block_size", "warmup_ratio", "lora_r", "lora_alpha", "lora_dropout", "weight_decay", "gradient_accumulation", "use_peft", "use_fp16", "use_int4", "push_to_hub", "repo_id", "preprocess_dataset", "prompt_column", "response_column", "prompt_prefix", "prompt_suffix", "response_prefix", "response_suffix", "error_log", "date_created", "last_modified", "platform"]

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
        """Create an instance of Training from a JSON string"""
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
            "date_created",
            "last_modified",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dataset
        if self.dataset:
            _dict['dataset'] = self.dataset.to_dict()
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Training from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "dataset": DataSet.from_dict(obj["dataset"]) if obj.get("dataset") is not None else None,
            "project_name": obj.get("project_name"),
            "metadata": obj.get("metadata"),
            "status": obj.get("status"),
            "retry_attempts": obj.get("retry_attempts"),
            "fine_tuned_model": obj.get("fine_tuned_model"),
            "provider": obj.get("provider"),
            "base_model_name": obj.get("base_model_name"),
            "text_column": obj.get("text_column"),
            "learning_rate": obj.get("learning_rate"),
            "batch_size": obj.get("batch_size"),
            "num_epochs": obj.get("num_epochs"),
            "block_size": obj.get("block_size"),
            "warmup_ratio": obj.get("warmup_ratio"),
            "lora_r": obj.get("lora_r"),
            "lora_alpha": obj.get("lora_alpha"),
            "lora_dropout": obj.get("lora_dropout"),
            "weight_decay": obj.get("weight_decay"),
            "gradient_accumulation": obj.get("gradient_accumulation"),
            "use_peft": obj.get("use_peft"),
            "use_fp16": obj.get("use_fp16"),
            "use_int4": obj.get("use_int4"),
            "push_to_hub": obj.get("push_to_hub"),
            "repo_id": obj.get("repo_id"),
            "preprocess_dataset": obj.get("preprocess_dataset"),
            "prompt_column": obj.get("prompt_column"),
            "response_column": obj.get("response_column"),
            "prompt_prefix": obj.get("prompt_prefix"),
            "prompt_suffix": obj.get("prompt_suffix"),
            "response_prefix": obj.get("response_prefix"),
            "response_suffix": obj.get("response_suffix"),
            "error_log": obj.get("error_log"),
            "date_created": obj.get("date_created"),
            "last_modified": obj.get("last_modified"),
            "platform": obj.get("platform")
        })
        return _obj


