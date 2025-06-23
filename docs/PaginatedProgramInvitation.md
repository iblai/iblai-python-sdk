# PaginatedProgramInvitation

Response serializer for paginated program invitation list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[ProgramInvitationDetail]**](ProgramInvitationDetail.md) | List of program invitations | 

## Example

```python
from iblai.models.paginated_program_invitation import PaginatedProgramInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProgramInvitation from a JSON string
paginated_program_invitation_instance = PaginatedProgramInvitation.from_json(json)
# print the JSON string representation of the object
print(PaginatedProgramInvitation.to_json())

# convert the object into a dict
paginated_program_invitation_dict = paginated_program_invitation_instance.to_dict()
# create an instance of PaginatedProgramInvitation from a dict
paginated_program_invitation_from_dict = PaginatedProgramInvitation.from_dict(paginated_program_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


