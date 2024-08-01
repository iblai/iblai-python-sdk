# UserMemoryContextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**platform_key** | **str** |  | 
**extra_data** | **str** |  | [optional] 
**use_reported_skills** | **bool** |  | [optional] 
**use_desired_skills** | **bool** |  | [optional] 
**use_credentials** | **bool** |  | [optional] 
**use_enrolled_courses** | **bool** |  | [optional] 
**use_time_spent** | **bool** |  | [optional] 
**use_completed_courses** | **bool** |  | [optional] 
**use_completed_programs** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_memory_context_response import UserMemoryContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemoryContextResponse from a JSON string
user_memory_context_response_instance = UserMemoryContextResponse.from_json(json)
# print the JSON string representation of the object
print(UserMemoryContextResponse.to_json())

# convert the object into a dict
user_memory_context_response_dict = user_memory_context_response_instance.to_dict()
# create an instance of UserMemoryContextResponse from a dict
user_memory_context_response_from_dict = UserMemoryContextResponse.from_dict(user_memory_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


