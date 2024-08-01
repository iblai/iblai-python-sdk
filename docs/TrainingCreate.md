# TrainingCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**project_name** | **str** |  | 
**dataset** | **str** |  | 
**base_model_name** | **str** |  | 
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
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.training_create import TrainingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingCreate from a JSON string
training_create_instance = TrainingCreate.from_json(json)
# print the JSON string representation of the object
print(TrainingCreate.to_json())

# convert the object into a dict
training_create_dict = training_create_instance.to_dict()
# create an instance of TrainingCreate from a dict
training_create_from_dict = TrainingCreate.from_dict(training_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


