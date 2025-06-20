# PlatformInvitationCreate

Request serializer for PlatformInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform to create an invitation for | 
**email** | **str** | The email address to invite | [optional] 
**username** | **str** | The username to invite | [optional] 
**active** | **bool** | Whether the invitation is active | [optional] [default to True]
**source** | **str** | The source of the invitation | [optional] 
**redirect_to** | **str** | URL to redirect to after accepting the invitation | [optional] 
**created** | **datetime** | When the invitation was created | [optional] 
**expired** | **datetime** | When the invitation expires | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | [optional] 

## Example

```python
from iblai.models.platform_invitation_create import PlatformInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformInvitationCreate from a JSON string
platform_invitation_create_instance = PlatformInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(PlatformInvitationCreate.to_json())

# convert the object into a dict
platform_invitation_create_dict = platform_invitation_create_instance.to_dict()
# create an instance of PlatformInvitationCreate from a dict
platform_invitation_create_from_dict = PlatformInvitationCreate.from_dict(platform_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


