# PermissionCheckRequest

Serializer for permission check requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key to check permissions for | 
**resources** | **List[str]** | List of resource paths to check permissions for. Must start and end with &#39;/&#39; (e.g., [&#39;/mentors/&#39;, &#39;/mentors/123/&#39;, &#39;/students/&#39;]) | 

## Example

```python
from iblai.models.permission_check_request import PermissionCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckRequest from a JSON string
permission_check_request_instance = PermissionCheckRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionCheckRequest.to_json())

# convert the object into a dict
permission_check_request_dict = permission_check_request_instance.to_dict()
# create an instance of PermissionCheckRequest from a dict
permission_check_request_from_dict = PermissionCheckRequest.from_dict(permission_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


