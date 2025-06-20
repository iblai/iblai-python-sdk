# BulkProgramInvitationResponse

Response serializer for bulk invitation creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **int** | Number of successfully created invitations | 
**error_codes** | **List[str]** | List of error codes for failed invitations | 

## Example

```python
from iblai.models.bulk_program_invitation_response import BulkProgramInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkProgramInvitationResponse from a JSON string
bulk_program_invitation_response_instance = BulkProgramInvitationResponse.from_json(json)
# print the JSON string representation of the object
print(BulkProgramInvitationResponse.to_json())

# convert the object into a dict
bulk_program_invitation_response_dict = bulk_program_invitation_response_instance.to_dict()
# create an instance of BulkProgramInvitationResponse from a dict
bulk_program_invitation_response_from_dict = BulkProgramInvitationResponse.from_dict(bulk_program_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


