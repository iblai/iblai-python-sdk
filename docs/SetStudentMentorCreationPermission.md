# SetStudentMentorCreationPermission

Serializer for setting student mentor creation permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform key where the permission should be changed | 
**allow_students_to_create_mentors** | **bool** | Whether to allow students to create mentors (true) or not (false) | 

## Example

```python
from iblai.models.set_student_mentor_creation_permission import SetStudentMentorCreationPermission

# TODO update the JSON string below
json = "{}"
# create an instance of SetStudentMentorCreationPermission from a JSON string
set_student_mentor_creation_permission_instance = SetStudentMentorCreationPermission.from_json(json)
# print the JSON string representation of the object
print(SetStudentMentorCreationPermission.to_json())

# convert the object into a dict
set_student_mentor_creation_permission_dict = set_student_mentor_creation_permission_instance.to_dict()
# create an instance of SetStudentMentorCreationPermission from a dict
set_student_mentor_creation_permission_from_dict = SetStudentMentorCreationPermission.from_dict(set_student_mentor_creation_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


