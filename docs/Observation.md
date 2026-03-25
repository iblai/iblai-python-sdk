# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**trace_id** | **str** |  | 
**type** | **str** |  | 
**parent_observation_id** | **str** |  | [optional] 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | [optional] 
**name** | **str** |  | 
**metadata** | **object** |  | 
**level** | **str** |  | 
**status_message** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**input** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**provided_model_name** | **str** |  | [optional] 
**internal_model_id** | **str** |  | [optional] 
**model_parameters** | **str** |  | [optional] 
**provided_usage_details** | **str** |  | 
**usage_details** | **str** |  | 
**provided_cost_details** | **str** |  | 
**cost_details** | **str** |  | 
**total_cost** | **decimal.Decimal** |  | [optional] 
**completion_start_time** | **datetime** |  | [optional] 
**prompt_id** | **str** |  | [optional] 
**prompt_name** | **str** |  | [optional] 
**prompt_version** | **int** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] 
**event_ts** | **datetime** |  | 
**is_deleted** | **int** |  | 

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


