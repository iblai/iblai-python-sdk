# BulkCourseInvitationResponse

Response serializer for bulk invitation creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **int** | Number of successfully created invitations | 
**error_codes** | **List[str]** | List of error codes for failed invitations | 

## Example

```python
from iblai.models.bulk_course_invitation_response import BulkCourseInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCourseInvitationResponse from a JSON string
bulk_course_invitation_response_instance = BulkCourseInvitationResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCourseInvitationResponse.to_json())

# convert the object into a dict
bulk_course_invitation_response_dict = bulk_course_invitation_response_instance.to_dict()
# create an instance of BulkCourseInvitationResponse from a dict
bulk_course_invitation_response_from_dict = BulkCourseInvitationResponse.from_dict(bulk_course_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


