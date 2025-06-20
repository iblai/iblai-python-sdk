# ManagerAuthToken

Manager auth token serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token key | [readonly] 
**expires** | **datetime** | Token expiration | 

## Example

```python
from iblai.models.manager_auth_token import ManagerAuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerAuthToken from a JSON string
manager_auth_token_instance = ManagerAuthToken.from_json(json)
# print the JSON string representation of the object
print(ManagerAuthToken.to_json())

# convert the object into a dict
manager_auth_token_dict = manager_auth_token_instance.to_dict()
# create an instance of ManagerAuthToken from a dict
manager_auth_token_from_dict = ManagerAuthToken.from_dict(manager_auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


