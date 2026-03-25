# UserMemoryEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 
**expires_at** | **str** |  | [optional] 

## Example

```python
from iblai.models.user_memory_entry_request import UserMemoryEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemoryEntryRequest from a JSON string
user_memory_entry_request_instance = UserMemoryEntryRequest.from_json(json)
# print the JSON string representation of the object
print(UserMemoryEntryRequest.to_json())

# convert the object into a dict
user_memory_entry_request_dict = user_memory_entry_request_instance.to_dict()
# create an instance of UserMemoryEntryRequest from a dict
user_memory_entry_request_from_dict = UserMemoryEntryRequest.from_dict(user_memory_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


