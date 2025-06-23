# CallAuthenticationResponse

Serializer for IBL Call Pro authentication parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ws_url** | **str** | The WebSocket URL for the IBL Call Pro server | 
**room_name** | **str** | The name of the IBL Call Pro room | 
**participant_name** | **str** | The name of the participant joining the room | 
**participant_token** | **str** | The JWT token for authenticating the participant | 

## Example

```python
from iblai.models.call_authentication_response import CallAuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallAuthenticationResponse from a JSON string
call_authentication_response_instance = CallAuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(CallAuthenticationResponse.to_json())

# convert the object into a dict
call_authentication_response_dict = call_authentication_response_instance.to_dict()
# create an instance of CallAuthenticationResponse from a dict
call_authentication_response_from_dict = CallAuthenticationResponse.from_dict(call_authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


