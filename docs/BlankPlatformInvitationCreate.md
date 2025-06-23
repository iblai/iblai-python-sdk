# BlankPlatformInvitationCreate

Request serializer for BlankPlatformInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform to create invitations for | 
**source** | **str** | The source identifier for the invitations | 
**count** | **int** | The number of blank invitations to create | 
**metadata** | **Dict[str, object]** | Additional metadata for the invitations | [optional] 

## Example

```python
from iblai.models.blank_platform_invitation_create import BlankPlatformInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BlankPlatformInvitationCreate from a JSON string
blank_platform_invitation_create_instance = BlankPlatformInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BlankPlatformInvitationCreate.to_json())

# convert the object into a dict
blank_platform_invitation_create_dict = blank_platform_invitation_create_instance.to_dict()
# create an instance of BlankPlatformInvitationCreate from a dict
blank_platform_invitation_create_from_dict = BlankPlatformInvitationCreate.from_dict(blank_platform_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


