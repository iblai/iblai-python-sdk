# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**trace_id** | **str** |  | 
**project_id** | **str** |  | 
**type** | **str** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | 
**name** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**parent_observation_id** | **str** |  | 
**level** | **str** |  | 
**status_message** | **str** |  | 
**version** | **str** |  | 
**created_at** | **datetime** |  | 
**model** | **str** |  | 
**model_parameters** | **Dict[str, object]** |  | 
**input** | **object** |  | 
**output** | **object** |  | 
**prompt_tokens** | **int** |  | 
**completion_tokens** | **int** |  | 
**total_tokens** | **int** |  | 
**unit** | **str** |  | 
**completion_start_time** | **datetime** |  | 
**prompt_id** | **str** |  | 
**usage** | **Dict[str, object]** |  | [optional] 
**price** | **float** |  | 

## Example

```python
from iblai.models.observation import Observation

# TODO update the JSON string below
json = "{}"
# create an instance of Observation from a JSON string
observation_instance = Observation.from_json(json)
# print the JSON string representation of the object
print(Observation.to_json())

# convert the object into a dict
observation_dict = observation_instance.to_dict()
# create an instance of Observation from a dict
observation_from_dict = Observation.from_dict(observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


