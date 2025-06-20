# BulkCourseInvitationCreate

Request serializer for BulkCourseInvitationView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_data** | [**List[CourseInvitationCreate]**](CourseInvitationCreate.md) | List of invitation data objects | 
**platform_key** | **str** | The platform key for permission validation | [optional] 

## Example

```python
from iblai.models.bulk_course_invitation_create import BulkCourseInvitationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCourseInvitationCreate from a JSON string
bulk_course_invitation_create_instance = BulkCourseInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(BulkCourseInvitationCreate.to_json())

# convert the object into a dict
bulk_course_invitation_create_dict = bulk_course_invitation_create_instance.to_dict()
# create an instance of BulkCourseInvitationCreate from a dict
bulk_course_invitation_create_from_dict = BulkCourseInvitationCreate.from_dict(bulk_course_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


