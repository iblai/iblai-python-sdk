# RedirectTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from iblai.models.redirect_token_request import RedirectTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectTokenRequest from a JSON string
redirect_token_request_instance = RedirectTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectTokenRequest.to_json())

# convert the object into a dict
redirect_token_request_dict = redirect_token_request_instance.to_dict()
# create an instance of RedirectTokenRequest from a dict
redirect_token_request_from_dict = RedirectTokenRequest.from_dict(redirect_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


