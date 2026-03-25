# SharedSessionUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_shared** | **bool** |  | 

## Example

```python
from iblai.models.shared_session_update_request import SharedSessionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedSessionUpdateRequest from a JSON string
shared_session_update_request_instance = SharedSessionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SharedSessionUpdateRequest.to_json())

# convert the object into a dict
shared_session_update_request_dict = shared_session_update_request_instance.to_dict()
# create an instance of SharedSessionUpdateRequest from a dict
shared_session_update_request_from_dict = SharedSessionUpdateRequest.from_dict(shared_session_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


