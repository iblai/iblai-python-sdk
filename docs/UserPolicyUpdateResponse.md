# UserPolicyUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **List[str]** | List of policies for the user | 

## Example

```python
from iblai.models.user_policy_update_response import UserPolicyUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPolicyUpdateResponse from a JSON string
user_policy_update_response_instance = UserPolicyUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(UserPolicyUpdateResponse.to_json())

# convert the object into a dict
user_policy_update_response_dict = user_policy_update_response_instance.to_dict()
# create an instance of UserPolicyUpdateResponse from a dict
user_policy_update_response_from_dict = UserPolicyUpdateResponse.from_dict(user_policy_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


