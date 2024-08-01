# UserMemoryContextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_data** | **str** | Extra custom data to be added to the memory | [optional] 
**use_reported_skills** | **bool** |  | [optional] 
**use_desired_skills** | **bool** |  | [optional] 
**use_credentials** | **bool** |  | [optional] 
**use_enrolled_courses** | **bool** |  | [optional] 
**use_time_spent** | **bool** |  | [optional] 
**use_completed_courses** | **bool** |  | [optional] 
**use_completed_programs** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_memory_context_request import UserMemoryContextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemoryContextRequest from a JSON string
user_memory_context_request_instance = UserMemoryContextRequest.from_json(json)
# print the JSON string representation of the object
print(UserMemoryContextRequest.to_json())

# convert the object into a dict
user_memory_context_request_dict = user_memory_context_request_instance.to_dict()
# create an instance of UserMemoryContextRequest from a dict
user_memory_context_request_from_dict = UserMemoryContextRequest.from_dict(user_memory_context_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


