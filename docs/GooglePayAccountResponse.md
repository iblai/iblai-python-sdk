# GooglePayAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**bundle_id** | **str** | The bundle id of the app | [optional] [default to '']
**status** | [**GooglePayAccountResponseStatusEnum**](GooglePayAccountResponseStatusEnum.md) |  | [optional] 
**created_on** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 
**user** | **int** | edX user ID | [optional] 

## Example

```python
from iblai.models.google_pay_account_response import GooglePayAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePayAccountResponse from a JSON string
google_pay_account_response_instance = GooglePayAccountResponse.from_json(json)
# print the JSON string representation of the object
print(GooglePayAccountResponse.to_json())

# convert the object into a dict
google_pay_account_response_dict = google_pay_account_response_instance.to_dict()
# create an instance of GooglePayAccountResponse from a dict
google_pay_account_response_from_dict = GooglePayAccountResponse.from_dict(google_pay_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


