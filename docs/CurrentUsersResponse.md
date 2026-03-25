# CurrentUsersResponse

Users currently active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] [default to 'currently_active']
**count** | **int** |  | 
**change** | **int** |  | 

## Example

```python
from iblai.models.current_users_response import CurrentUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUsersResponse from a JSON string
current_users_response_instance = CurrentUsersResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentUsersResponse.to_json())

# convert the object into a dict
current_users_response_dict = current_users_response_instance.to_dict()
# create an instance of CurrentUsersResponse from a dict
current_users_response_from_dict = CurrentUsersResponse.from_dict(current_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


