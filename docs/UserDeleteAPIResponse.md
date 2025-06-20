# UserDeleteAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from iblai.models.user_delete_api_response import UserDeleteAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteAPIResponse from a JSON string
user_delete_api_response_instance = UserDeleteAPIResponse.from_json(json)
# print the JSON string representation of the object
print(UserDeleteAPIResponse.to_json())

# convert the object into a dict
user_delete_api_response_dict = user_delete_api_response_instance.to_dict()
# create an instance of UserDeleteAPIResponse from a dict
user_delete_api_response_from_dict = UserDeleteAPIResponse.from_dict(user_delete_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


