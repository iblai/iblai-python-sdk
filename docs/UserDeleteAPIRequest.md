# UserDeleteAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 

## Example

```python
from iblai.models.user_delete_api_request import UserDeleteAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteAPIRequest from a JSON string
user_delete_api_request_instance = UserDeleteAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UserDeleteAPIRequest.to_json())

# convert the object into a dict
user_delete_api_request_dict = user_delete_api_request_instance.to_dict()
# create an instance of UserDeleteAPIRequest from a dict
user_delete_api_request_from_dict = UserDeleteAPIRequest.from_dict(user_delete_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


