# UserPolicyUpdate

Serializer for updating user policies on a platform.  Accepts lists of policies to add and remove for a specific user on a platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | ID of the user to update policies for | 
**platform_key** | **str** | Platform key where the user&#39;s policies should be updated | 
**policies_to_add** | **List[str]** | List of policy names to add to the user | [optional] 
**policies_to_remove** | **List[str]** | List of policy names to remove from the user | [optional] 
**policies_to_set** | **List[str]** | List of policy names to set for the user (replaces all existing policies with these) | [optional] 

## Example

```python
from iblai.models.user_policy_update import UserPolicyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserPolicyUpdate from a JSON string
user_policy_update_instance = UserPolicyUpdate.from_json(json)
# print the JSON string representation of the object
print(UserPolicyUpdate.to_json())

# convert the object into a dict
user_policy_update_dict = user_policy_update_instance.to_dict()
# create an instance of UserPolicyUpdate from a dict
user_policy_update_from_dict = UserPolicyUpdate.from_dict(user_policy_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


