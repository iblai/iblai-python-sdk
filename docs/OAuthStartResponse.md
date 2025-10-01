# OAuthStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** |  | 

## Example

```python
from iblai.models.o_auth_start_response import OAuthStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthStartResponse from a JSON string
o_auth_start_response_instance = OAuthStartResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthStartResponse.to_json())

# convert the object into a dict
o_auth_start_response_dict = o_auth_start_response_instance.to_dict()
# create an instance of OAuthStartResponse from a dict
o_auth_start_response_from_dict = OAuthStartResponse.from_dict(o_auth_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


