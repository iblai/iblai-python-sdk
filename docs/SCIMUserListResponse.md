# SCIMUserListResponse

SCIM user list response serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | 
**total_results** | **int** | Total number of results | 
**resources** | **List[Dict[str, object]]** | List of user resources | 

## Example

```python
from iblai.models.scim_user_list_response import SCIMUserListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMUserListResponse from a JSON string
scim_user_list_response_instance = SCIMUserListResponse.from_json(json)
# print the JSON string representation of the object
print(SCIMUserListResponse.to_json())

# convert the object into a dict
scim_user_list_response_dict = scim_user_list_response_instance.to_dict()
# create an instance of SCIMUserListResponse from a dict
scim_user_list_response_from_dict = SCIMUserListResponse.from_dict(scim_user_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


