# MarkAllReadResponse

Serializer for the response when marking all notifications as read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from iblai.models.mark_all_read_response import MarkAllReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAllReadResponse from a JSON string
mark_all_read_response_instance = MarkAllReadResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAllReadResponse.to_json())

# convert the object into a dict
mark_all_read_response_dict = mark_all_read_response_instance.to_dict()
# create an instance of MarkAllReadResponse from a dict
mark_all_read_response_from_dict = MarkAllReadResponse.from_dict(mark_all_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


