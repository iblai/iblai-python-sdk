# ResourceCompletion

Serializer for resource completion data used in both request and response. Inherits common completion fields from CompletableBaseSerializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_percentage** | **float** | Completion percentage | [optional] 
**completed** | **bool** | Whether completable is completed | [optional] [default to False]
**last_updated** | **datetime** | Last update timestamp | [readonly] 
**completion_date** | **datetime** | Completion timestamp | [optional] 
**completion_data** | **object** | Completion metadata | [optional] 
**skill_points_computed** | **bool** | Whether skill points have been evaluated | [optional] [default to False]
**resource_id** | **int** | The unique identifier for the resource | 
**resource_type** | **str** | The type of resource | 
**user_id** | **int** | The user identifier | 
**username** | **str** | The username associated with the completion | [readonly] 

## Example

```python
from iblai.models.resource_completion import ResourceCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCompletion from a JSON string
resource_completion_instance = ResourceCompletion.from_json(json)
# print the JSON string representation of the object
print(ResourceCompletion.to_json())

# convert the object into a dict
resource_completion_dict = resource_completion_instance.to_dict()
# create an instance of ResourceCompletion from a dict
resource_completion_from_dict = ResourceCompletion.from_dict(resource_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


