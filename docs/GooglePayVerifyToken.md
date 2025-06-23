# GooglePayVerifyToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_pay_receipt** | **str** |  | 
**bundle_id** | **str** |  | [optional] [default to 'ai.ibl.mentorai']
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from iblai.models.google_pay_verify_token import GooglePayVerifyToken

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePayVerifyToken from a JSON string
google_pay_verify_token_instance = GooglePayVerifyToken.from_json(json)
# print the JSON string representation of the object
print(GooglePayVerifyToken.to_json())

# convert the object into a dict
google_pay_verify_token_dict = google_pay_verify_token_instance.to_dict()
# create an instance of GooglePayVerifyToken from a dict
google_pay_verify_token_from_dict = GooglePayVerifyToken.from_dict(google_pay_verify_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


