# ProgramInvitationRedemption

Request serializer for ProgramInvitationRedemptionView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_key** | **str** | The program key for the invitation | 
**source** | **str** | The source identifier for the invitation | 
**email** | **str** | The email to associate with the invitation | [optional] 
**username** | **str** | The username to associate with the invitation | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | [optional] 

## Example

```python
from iblai.models.program_invitation_redemption import ProgramInvitationRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramInvitationRedemption from a JSON string
program_invitation_redemption_instance = ProgramInvitationRedemption.from_json(json)
# print the JSON string representation of the object
print(ProgramInvitationRedemption.to_json())

# convert the object into a dict
program_invitation_redemption_dict = program_invitation_redemption_instance.to_dict()
# create an instance of ProgramInvitationRedemption from a dict
program_invitation_redemption_from_dict = ProgramInvitationRedemption.from_dict(program_invitation_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


