# RbacUser

Serializer for users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | edX user ID | [readonly] 
**username** | **str** | edX username | [optional] 

## Example

```python
from iblai.models.rbac_user import RbacUser

# TODO update the JSON string below
json = "{}"
# create an instance of RbacUser from a JSON string
rbac_user_instance = RbacUser.from_json(json)
# print the JSON string representation of the object
print(RbacUser.to_json())

# convert the object into a dict
rbac_user_dict = rbac_user_instance.to_dict()
# create an instance of RbacUser from a dict
rbac_user_from_dict = RbacUser.from_dict(rbac_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


