# BulkPlatformInvitationCreate

Request serializer for BulkPlatformInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_data** | [**List[PlatformInvitationCreate]**](PlatformInvitationCreate.md) | List of invitation data objects | 
**platform_key** | **str** | The platform key for permission validation | [optional] 

## Example

```python
from iblai.models.bulk_platform_invitation_create import BulkPlatformInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPlatformInvitationCreate from a JSON string
bulk_platform_invitation_create_instance = BulkPlatformInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BulkPlatformInvitationCreate.to_json())

# convert the object into a dict
bulk_platform_invitation_create_dict = bulk_platform_invitation_create_instance.to_dict()
# create an instance of BulkPlatformInvitationCreate from a dict
bulk_platform_invitation_create_from_dict = BulkPlatformInvitationCreate.from_dict(bulk_platform_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


