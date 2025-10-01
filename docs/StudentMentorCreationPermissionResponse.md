# StudentMentorCreationPermissionResponse

Serializer for student mentor creation permission responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_students_to_create_mentors** | **bool** | Whether students can create mentors on this platform | 
**platform_key** | **str** | The platform key | 
**message** | **str** | Success message (only in set permission response) | [optional] 

## Example

```python
from iblai.models.student_mentor_creation_permission_response import StudentMentorCreationPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StudentMentorCreationPermissionResponse from a JSON string
student_mentor_creation_permission_response_instance = StudentMentorCreationPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(StudentMentorCreationPermissionResponse.to_json())

# convert the object into a dict
student_mentor_creation_permission_response_dict = student_mentor_creation_permission_response_instance.to_dict()
# create an instance of StudentMentorCreationPermissionResponse from a dict
student_mentor_creation_permission_response_from_dict = StudentMentorCreationPermissionResponse.from_dict(student_mentor_creation_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


