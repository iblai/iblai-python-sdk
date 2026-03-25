# PlatformMembershipConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [readonly] 
**platform_name** | **str** |  | [readonly] 
**allow_self_linking** | **bool** | Whether users can self-link to this platform | [optional] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.platform_membership_config import PlatformMembershipConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformMembershipConfig from a JSON string
platform_membership_config_instance = PlatformMembershipConfig.from_json(json)
# print the JSON string representation of the object
print(PlatformMembershipConfig.to_json())

# convert the object into a dict
platform_membership_config_dict = platform_membership_config_instance.to_dict()
# create an instance of PlatformMembershipConfig from a dict
platform_membership_config_from_dict = PlatformMembershipConfig.from_dict(platform_membership_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


