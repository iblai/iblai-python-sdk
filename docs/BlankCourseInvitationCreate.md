# BlankCourseInvitationCreate

Request serializer for BlankCourseInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course to create invitations for | 
**source** | **str** | The source identifier for the invitations | 
**count** | **int** | The number of blank invitations to create | 
**metadata** | **Dict[str, object]** | Additional metadata for the invitations | [optional] 

## Example

```python
from iblai.models.blank_course_invitation_create import BlankCourseInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BlankCourseInvitationCreate from a JSON string
blank_course_invitation_create_instance = BlankCourseInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BlankCourseInvitationCreate.to_json())

# convert the object into a dict
blank_course_invitation_create_dict = blank_course_invitation_create_instance.to_dict()
# create an instance of BlankCourseInvitationCreate from a dict
blank_course_invitation_create_from_dict = BlankCourseInvitationCreate.from_dict(blank_course_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


