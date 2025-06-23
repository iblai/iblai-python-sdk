# ProgramInvitationDetail

Response serializer for program invitation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the invitation | 
**user_id** | **int** | The ID of the user associated with the invitation | 
**username** | **str** | The username of the user associated with the invitation | 
**email** | **str** | The email address associated with the invitation | 
**created** | **datetime** | When the invitation was created | 
**started** | **datetime** | When the invitation was started | 
**expired** | **datetime** | When the invitation expires | 
**source** | **str** | The source of the invitation | 
**redirect_to** | **str** | URL to redirect to after accepting the invitation | 
**active** | **bool** | Whether the invitation is active | 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | 
**program_key** | **str** | The program key associated with the invitation | 

## Example

```python
from iblai.models.program_invitation_detail import ProgramInvitationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramInvitationDetail from a JSON string
program_invitation_detail_instance = ProgramInvitationDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramInvitationDetail.to_json())

# convert the object into a dict
program_invitation_detail_dict = program_invitation_detail_instance.to_dict()
# create an instance of ProgramInvitationDetail from a dict
program_invitation_detail_from_dict = ProgramInvitationDetail.from_dict(program_invitation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


