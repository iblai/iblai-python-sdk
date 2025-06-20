# CallAuthenticationRequest

Serializer for IBL Call Pro authentication request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | The ID of the session for the call | 
**pathway** | **str** | The pathway identifier for the call context | 

## Example

```python
from iblai.models.call_authentication_request import CallAuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallAuthenticationRequest from a JSON string
call_authentication_request_instance = CallAuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(CallAuthenticationRequest.to_json())

# convert the object into a dict
call_authentication_request_dict = call_authentication_request_instance.to_dict()
# create an instance of CallAuthenticationRequest from a dict
call_authentication_request_from_dict = CallAuthenticationRequest.from_dict(call_authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


