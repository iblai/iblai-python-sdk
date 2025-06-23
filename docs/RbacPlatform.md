# RbacPlatform

Serializer for platforms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**key** | **str** | The platform key | 
**name** | **str** | The name of the platform | [optional] 

## Example

```python
from iblai.models.rbac_platform import RbacPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of RbacPlatform from a JSON string
rbac_platform_instance = RbacPlatform.from_json(json)
# print the JSON string representation of the object
print(RbacPlatform.to_json())

# convert the object into a dict
rbac_platform_dict = rbac_platform_instance.to_dict()
# create an instance of RbacPlatform from a dict
rbac_platform_from_dict = RbacPlatform.from_dict(rbac_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


