# UserGroupAccessInfo

Serializer for group access information in responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Group ID | 
**name** | **str** | Group name | 
**description** | **str** | Group description | 
**permissions** | **List[str]** | List of permissions user has for this group (e.g., [&#39;read&#39;, &#39;manageMentors&#39;]) | 

## Example

```python
from iblai.models.user_group_access_info import UserGroupAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupAccessInfo from a JSON string
user_group_access_info_instance = UserGroupAccessInfo.from_json(json)
# print the JSON string representation of the object
print(UserGroupAccessInfo.to_json())

# convert the object into a dict
user_group_access_info_dict = user_group_access_info_instance.to_dict()
# create an instance of UserGroupAccessInfo from a dict
user_group_access_info_from_dict = UserGroupAccessInfo.from_dict(user_group_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


