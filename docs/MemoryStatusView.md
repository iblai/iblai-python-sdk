# MemoryStatusView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | 
**platform_key** | **str** |  | 
**enabled** | **bool** |  | [optional] 

## Example

```python
from iblai.models.memory_status_view import MemoryStatusView

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryStatusView from a JSON string
memory_status_view_instance = MemoryStatusView.from_json(json)
# print the JSON string representation of the object
print(MemoryStatusView.to_json())

# convert the object into a dict
memory_status_view_dict = memory_status_view_instance.to_dict()
# create an instance of MemoryStatusView from a dict
memory_status_view_from_dict = MemoryStatusView.from_dict(memory_status_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


