# PatchedTrainingCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**project_name** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**base_model_name** | **str** |  | [optional] 
**provider** | [**Provider63aEnum**](Provider63aEnum.md) |  | [optional] 
**text_column** | **str** |  | [optional] 
**learning_rate** | **float** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**num_epochs** | **int** |  | [optional] 
**block_size** | **int** |  | [optional] 
**warmup_ratio** | **float** |  | [optional] 
**lora_r** | **int** |  | [optional] 
**lora_alpha** | **int** |  | [optional] 
**lora_dropout** | **float** |  | [optional] 
**weight_decay** | **float** |  | [optional] 
**gradient_accumulation** | **int** |  | [optional] 
**use_peft** | **bool** |  | [optional] 
**use_fp16** | **bool** |  | [optional] 
**use_int4** | **bool** |  | [optional] 
**push_to_hub** | **bool** |  | [optional] 
**repo_id** | **str** |  | [optional] 
**preprocess_dataset** | **bool** |  | [optional] 
**prompt_column** | **str** |  | [optional] 
**prompt_prefix** | **str** |  | [optional] 
**prompt_suffix** | **str** |  | [optional] 
**response_prefix** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_training_create import PatchedTrainingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTrainingCreate from a JSON string
patched_training_create_instance = PatchedTrainingCreate.from_json(json)
# print the JSON string representation of the object
print(PatchedTrainingCreate.to_json())

# convert the object into a dict
patched_training_create_dict = patched_training_create_instance.to_dict()
# create an instance of PatchedTrainingCreate from a dict
patched_training_create_from_dict = PatchedTrainingCreate.from_dict(patched_training_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


