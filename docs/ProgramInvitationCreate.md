# ProgramInvitationCreate

Request serializer for ProgramInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_key** | **str** | The program to create an invitation for | 
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
from iblai.models.program_invitation_create import ProgramInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramInvitationCreate from a JSON string
program_invitation_create_instance = ProgramInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramInvitationCreate.to_json())

# convert the object into a dict
program_invitation_create_dict = program_invitation_create_instance.to_dict()
# create an instance of ProgramInvitationCreate from a dict
program_invitation_create_from_dict = ProgramInvitationCreate.from_dict(program_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


