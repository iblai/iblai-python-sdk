# BulkProgramInvitationCreate

Request serializer for BulkProgramInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_data** | [**List[ProgramInvitationCreate]**](ProgramInvitationCreate.md) | List of invitation data objects | 
**platform_key** | **str** | The platform key for permission validation | [optional] 

## Example

```python
from iblai.models.bulk_program_invitation_create import BulkProgramInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkProgramInvitationCreate from a JSON string
bulk_program_invitation_create_instance = BulkProgramInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BulkProgramInvitationCreate.to_json())

# convert the object into a dict
bulk_program_invitation_create_dict = bulk_program_invitation_create_instance.to_dict()
# create an instance of BulkProgramInvitationCreate from a dict
bulk_program_invitation_create_from_dict = BulkProgramInvitationCreate.from_dict(bulk_program_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


