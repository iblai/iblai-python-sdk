# PlatformInvitationDetail

Response serializer for platform invitation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the invitation | 
**user_id** | **int** | The ID of the user associated with the invitation | [optional] 
**username** | **str** | The username of the user associated with the invitation | 
**email** | **str** | The email address associated with the invitation | 
**created** | **datetime** | When the invitation was created | [optional] 
**started** | **datetime** | When the invitation was started | 
**expired** | **datetime** | When the invitation expires | 
**source** | **str** | The source of the invitation | 
**redirect_to** | **str** | URL to redirect to after accepting the invitation | 
**active** | **bool** | Whether the invitation is active | 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | 
**platform_key** | **str** | The platform key associated with the invitation | 

## Example

```python
from iblai.models.platform_invitation_detail import PlatformInvitationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformInvitationDetail from a JSON string
platform_invitation_detail_instance = PlatformInvitationDetail.from_json(json)
# print the JSON string representation of the object
print(PlatformInvitationDetail.to_json())

# convert the object into a dict
platform_invitation_detail_dict = platform_invitation_detail_instance.to_dict()
# create an instance of PlatformInvitationDetail from a dict
platform_invitation_detail_from_dict = PlatformInvitationDetail.from_dict(platform_invitation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


