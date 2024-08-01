# UserEdxMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | [readonly] 
**student** | **int** | edX user ID | 
**course_id** | **str** |  | 
**data** | **object** | The course data to be stored. This includes the current page and the blocks that have been visited. | [optional] 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.user_edx_memory import UserEdxMemory

# TODO update the JSON string below
json = "{}"
# create an instance of UserEdxMemory from a JSON string
user_edx_memory_instance = UserEdxMemory.from_json(json)
# print the JSON string representation of the object
print(UserEdxMemory.to_json())

# convert the object into a dict
user_edx_memory_dict = user_edx_memory_instance.to_dict()
# create an instance of UserEdxMemory from a dict
user_edx_memory_from_dict = UserEdxMemory.from_dict(user_edx_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


