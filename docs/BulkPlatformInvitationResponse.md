# BulkPlatformInvitationResponse

Response serializer for bulk invitation creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **int** | Number of successfully created invitations | 
**error_codes** | **List[str]** | List of error codes for failed invitations | 

## Example

```python
from iblai.models.bulk_platform_invitation_response import BulkPlatformInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPlatformInvitationResponse from a JSON string
bulk_platform_invitation_response_instance = BulkPlatformInvitationResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPlatformInvitationResponse.to_json())

# convert the object into a dict
bulk_platform_invitation_response_dict = bulk_platform_invitation_response_instance.to_dict()
# create an instance of BulkPlatformInvitationResponse from a dict
bulk_platform_invitation_response_from_dict = BulkPlatformInvitationResponse.from_dict(bulk_platform_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


