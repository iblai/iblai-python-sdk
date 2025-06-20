# UserDeleteAPIError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 

## Example

```python
from iblai.models.user_delete_api_error import UserDeleteAPIError

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteAPIError from a JSON string
user_delete_api_error_instance = UserDeleteAPIError.from_json(json)
# print the JSON string representation of the object
print(UserDeleteAPIError.to_json())

# convert the object into a dict
user_delete_api_error_dict = user_delete_api_error_instance.to_dict()
# create an instance of UserDeleteAPIError from a dict
user_delete_api_error_from_dict = UserDeleteAPIError.from_dict(user_delete_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


