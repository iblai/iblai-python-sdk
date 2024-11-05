# RedirectTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [readonly] 
**url** | **str** |  | 
**token** | **str** |  | [readonly] 

## Example

```python
from iblai.models.redirect_token_response import RedirectTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectTokenResponse from a JSON string
redirect_token_response_instance = RedirectTokenResponse.from_json(json)
# print the JSON string representation of the object
print(RedirectTokenResponse.to_json())

# convert the object into a dict
redirect_token_response_dict = redirect_token_response_instance.to_dict()
# create an instance of RedirectTokenResponse from a dict
redirect_token_response_from_dict = RedirectTokenResponse.from_dict(redirect_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


