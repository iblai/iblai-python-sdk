# MemoryStatusRequestView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable memory use | 

## Example

```python
from iblai.models.memory_status_request_view import MemoryStatusRequestView

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryStatusRequestView from a JSON string
memory_status_request_view_instance = MemoryStatusRequestView.from_json(json)
# print the JSON string representation of the object
print(MemoryStatusRequestView.to_json())

# convert the object into a dict
memory_status_request_view_dict = memory_status_request_view_instance.to_dict()
# create an instance of MemoryStatusRequestView from a dict
memory_status_request_view_from_dict = MemoryStatusRequestView.from_dict(memory_status_request_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


