# PlatformInvitationRedemption

Request serializer for PlatformInvitationRedemptionView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform key for the invitation | 
**source** | **str** | The source identifier for the invitation | 
**email** | **str** | The email to associate with the invitation | [optional] 
**username** | **str** | The username to associate with the invitation | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | [optional] 

## Example

```python
from iblai.models.platform_invitation_redemption import PlatformInvitationRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformInvitationRedemption from a JSON string
platform_invitation_redemption_instance = PlatformInvitationRedemption.from_json(json)
# print the JSON string representation of the object
print(PlatformInvitationRedemption.to_json())

# convert the object into a dict
platform_invitation_redemption_dict = platform_invitation_redemption_instance.to_dict()
# create an instance of PlatformInvitationRedemption from a dict
platform_invitation_redemption_from_dict = PlatformInvitationRedemption.from_dict(platform_invitation_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


