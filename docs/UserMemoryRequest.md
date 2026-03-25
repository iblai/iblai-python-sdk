# UserMemoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] [default to 'all']
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**mentor_unique_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**catalog_item_type** | **str** |  | [optional] 
**catalog_item_id** | **str** |  | [optional] 
**entries** | [**List[UserMemoryEntryRequest]**](UserMemoryEntryRequest.md) |  | 
**category** | **str** |  | [optional] 

## Example

```python
from iblai.models.user_memory_request import UserMemoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemoryRequest from a JSON string
user_memory_request_instance = UserMemoryRequest.from_json(json)
# print the JSON string representation of the object
print(UserMemoryRequest.to_json())

# convert the object into a dict
user_memory_request_dict = user_memory_request_instance.to_dict()
# create an instance of UserMemoryRequest from a dict
user_memory_request_from_dict = UserMemoryRequest.from_dict(user_memory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


