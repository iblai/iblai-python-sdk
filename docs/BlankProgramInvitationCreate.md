# BlankProgramInvitationCreate

Request serializer for BlankProgramInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_key** | **str** | The program to create invitations for | 
**source** | **str** | The source identifier for the invitations | 
**count** | **int** | The number of blank invitations to create | 
**metadata** | **Dict[str, object]** | Additional metadata for the invitations | [optional] 

## Example

```python
from iblai.models.blank_program_invitation_create import BlankProgramInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BlankProgramInvitationCreate from a JSON string
blank_program_invitation_create_instance = BlankProgramInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BlankProgramInvitationCreate.to_json())

# convert the object into a dict
blank_program_invitation_create_dict = blank_program_invitation_create_instance.to_dict()
# create an instance of BlankProgramInvitationCreate from a dict
blank_program_invitation_create_from_dict = BlankProgramInvitationCreate.from_dict(blank_program_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


