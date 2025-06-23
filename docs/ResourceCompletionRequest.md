# ResourceCompletionRequest

Request serializer for ResourceCompletionManagementView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** | The unique identifier for the resource | 
**user_id** | **int** | The ID of the user | 
**completed** | **bool** | Whether the resource is completed | [optional] 
**completion_percentage** | **float** | Percentage of completion (0.0-1.0) | [optional] 
**completion_date** | **datetime** | When the resource was completed | [optional] 
**completion_data** | **object** | Additional completion metadata | [optional] 

## Example

```python
from iblai.models.resource_completion_request import ResourceCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCompletionRequest from a JSON string
resource_completion_request_instance = ResourceCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceCompletionRequest.to_json())

# convert the object into a dict
resource_completion_request_dict = resource_completion_request_instance.to_dict()
# create an instance of ResourceCompletionRequest from a dict
resource_completion_request_from_dict = ResourceCompletionRequest.from_dict(resource_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


