# PlatformMembershipConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | 
**allow_self_linking** | **bool** |  | 

## Example

```python
from iblai.models.platform_membership_config_post_request import PlatformMembershipConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformMembershipConfigPostRequest from a JSON string
platform_membership_config_post_request_instance = PlatformMembershipConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformMembershipConfigPostRequest.to_json())

# convert the object into a dict
platform_membership_config_post_request_dict = platform_membership_config_post_request_instance.to_dict()
# create an instance of PlatformMembershipConfigPostRequest from a dict
platform_membership_config_post_request_from_dict = PlatformMembershipConfigPostRequest.from_dict(platform_membership_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


